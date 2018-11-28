#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

void read_arrangement(unsigned int *row, unsigned int* arrangement) {
    cin >> (*row);
    (*row) -= 1;
    for(int i=0; i < 16; i++)
    {
        cin >> arrangement[i];
    }
}

int main() {
    unsigned int cases;
    
    cin >> cases;
    
    for(unsigned int k=1; k<=cases; k++)
    {
        unsigned int row_a;
        unsigned int row_b;

        unsigned int arrangement_a[16];
        unsigned int arrangement_b[16];
        
        read_arrangement(&row_a, &arrangement_a[0]);
        
        read_arrangement(&row_b, &arrangement_b[0]);
        
        vector<int> values;
        int start_a = row_a*4;
        int start_b = row_b*4;
        for(int i=start_a; i<start_a+4; i++)
        {
            for(int j=start_b; j<start_b+4; j++)
            {
                if(arrangement_a[i] == arrangement_b[j])
                {
                    values.push_back(arrangement_a[i]);
                }
            }
        }
        
        cout << "Case #" << k << ": "; 
        if(values.empty())
        {
            cout << "Volunteer cheated!";
        }
        else
        if(values.size() == 1)
        {
            cout << values[0];
        }
        else
        {
           cout << "Bad magician!";
        }
        
        cout << endl;
        
    }
    return 0;
}
