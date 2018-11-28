#include <fstream>
#include <sstream>
#include <vector>
#include <map>

std::vector<int> splitDigits(int value) {
    std::stringstream s;
    s << value;
    std::string str = s.str();
    std::vector<int> result;
    result.reserve(str.size());
    for (size_t i = 0; i < str.size(); i++) {
        std::string d;
        d.append(1, str[i]);
        std::stringstream s2(d);
        int value;
        s2 >> value;
        result.push_back(value);
    }
    return result;
}

int processValue(int value) {
    if (value == 0) {
        return -1;
    }
    long currentValue = value;
    long currentMultiply = 2;
    std::map<int,int> map;
    for (int i = 0; i <=9; i++) {
        map[i] = 0;
    }
    while (true) {
        std::vector<int> digits = splitDigits(currentValue);

        for (std::vector<int>::iterator i = digits.begin(); i != digits.end(); ++i) {
            map[*i]++;
        }
        bool allSet = true;
        for (int i = 0; i <=9; i++) {
            if (map[i] == 0) {
                allSet = false;
                break;
            }
        }
        if (allSet) {
            return currentValue;
        }
        else {
            currentValue = value * currentMultiply;
            ++currentMultiply;
            if (currentValue == 100000000) {
                return -1;
            }
        }
    }
    return 0;
}

int main()
{
    std::ifstream file("in.txt");
    if (file)
    {
        /*
         * Get the size of the file
         */
        file.seekg(0,std::ios::end);
        std::streampos          length = file.tellg();
        file.seekg(0,std::ios::beg);

        /*
         * Use a vector as the buffer.
         * It is exception safe and will be tidied up correctly.
         * This constructor creates a buffer of the correct length.
         *
         * Then read the whole file into the buffer.
         */
        std::vector<char>       buffer(length);
        file.read(&buffer[0],length);

        /*
         * Create your string stream.
         * Get the stringbuffer from the stream and set the vector as it source.
         */
        std::stringstream       localStream;
        localStream.rdbuf()->pubsetbuf(&buffer[0],length);

        /*
         * Note the buffer is NOT copied, if it goes out of scope
         * the stream will be reading from released memory.
         */
        int N;
        localStream >> N;
        std::ofstream out("out.txt");
        for (int i = 1; i <= N;i++) {
            int value;
            localStream >> value;
            int result = processValue(value);
            out << "Case #" << i << ": ";
            if (result >= 0)
                out << result;
            else
                out << "INSOMNIA";
            out << std::endl;
        }
    }
}
