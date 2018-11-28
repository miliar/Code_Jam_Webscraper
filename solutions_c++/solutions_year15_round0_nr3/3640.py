#include <iostream>
using std::cin;
using std::cout;
using std::endl;

#include <fstream>
using std::ifstream;

#include <cassert>

#define NUM_COMPONENTS 3
static const char components[] = {'i', 'j', 'k'};

// Minimal Quaternion class representation (no magnitude)
class Quaternion
{
// private:
public:
    bool negative;
    char component;

public:
    Quaternion(char c): negative(0), component(c) {};
    bool is(char c) { return component == c? !negative: 0; };
    void cross(char c);
    void reset() { negative = 0; component = '1'; };
};

// Returns the "next" component
// Used for simplifying cross products
char next(char component)
{
    switch (component)
    {
        case 'i':   return 'j';
        case 'j':   return 'k';
        case 'k':   return 'i';
        default :   return '0';
    }
}

// Multiply simple quaternions
void Quaternion::cross(char c)
{
    // If currently 1
    if (component == '1')
    {
        component = c;
        return;
    }

    // If same
    if (component == c)
    {
        component = '1';
        negative = !negative;
    }

    // If other
    else
    {
        // If positive resultant
        if (c == next(component))
            component = next(c);

        // If negative resultant
        else
        {
            component = next(component);
            negative = !negative;
        }
    }
}



int main(int argc, char* argv[])
{
    // Open file
    char* filename;
    filename = argv[1];
    ifstream fs(filename);
    assert(fs.is_open());

    // Get number of cases
    int N_cases;
    fs >> N_cases;

    // Ignore trailing whitespace
    fs.ignore();

    // For every case...
    for (int i = 0; i < N_cases; ++i)
    {
        // Initialize and retrieve data set
        int base_size;
        fs >> base_size;

        int num_repeats;
        fs >> num_repeats;

        char base_string[base_size];
        fs >> base_string;

        // Create string to be evaluated
        int string_size = base_size * num_repeats;
        char out_str[string_size];
        for (int j = 0; j < string_size; ++j)
        {
            out_str[j] = base_string[j % base_size];
        }

        // Begin multiplying quaternions
        int completed = 0;
        char* str_iter = out_str;
        char target = components[completed];
        Quaternion quat('1');
        while (completed < NUM_COMPONENTS && completed != -1)
        {
            // Cross the quaternions
            quat.cross(*str_iter);

            // If found match
            if (quat.is(target))
            {
                completed++;
                target = components[completed % NUM_COMPONENTS];
                if (completed != NUM_COMPONENTS)
                    quat.reset();
            }

            str_iter++;

            // If at end and did not find split
            if (str_iter - out_str == string_size && completed != NUM_COMPONENTS)
                completed = -1;

            // If found split but not at end
            if (completed == NUM_COMPONENTS && str_iter - out_str != string_size)
                target = components[--completed];
        }

        const char* result = completed == NUM_COMPONENTS? "YES":"NO";

        // Print case number
        cout << "Case #" << i + 1 << ": ";
        cout << result << endl;
    }
}
