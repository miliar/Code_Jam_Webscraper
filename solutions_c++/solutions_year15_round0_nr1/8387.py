#include <fstream>
#include <iostream>

int main()
{
    std::ifstream in("input.txt");
    std::ofstream out("output.txt");
    
    int T, s_max;
    std::string str;
    
    int standing;
    int friends;
    
    in >> T;
    
    for (int i = 0; i < T; ++i) {
        standing = 0;
        friends = 0;
        
        in >> s_max;
        in >> str;
        
        for (int j = 0; j < str.length(); ++j) {
            if (str[j] != '0') {
                if (standing >= j) {
                    standing += str[j] - '0';
                } else {
                    int need = j - standing;
                    friends += need;
                    standing += need;
                    standing += str[j] - '0';
                }
            }
        }
        
        out << "Case #" << i + 1 << ": " << friends << std::endl;
    }
    
    in.close();
    out.close();
    
    return 0;
}