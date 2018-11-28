#include <iostream>
#include <fstream>
#include <vector>
#include <string>

class A{
public:
    A(std::string, int);
    ~A();
    int cal();

private:
    std::string name;
    int n;
    bool contantConsecutiveConsonants(int, int);
    bool isConsonants(char);
};

A::A(std::string s, int num){
    name = s;
    n = num;
}

A::~A(){
}

bool A::isConsonants(char c){
    if (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u')
        return true;
    else
        return false;
}

bool A::contantConsecutiveConsonants(int start, int end) {
    int countOfConsonants = 0;
    for (int i = start; i <= end; i++) {
        char c = name[i];
        if (isConsonants(c)) {
            countOfConsonants++;
            if (countOfConsonants >= n)
                return true;
        }
        else
            countOfConsonants = 0;
    }
    return false;
}

int A::cal(){
    int count = 0;
    for (int i = 0; i < name.size(); i++) {
        int j = i + n - 1;
        for (; j < name.size(); j++) {
            if(contantConsecutiveConsonants(i, j)) {
                count++;
            }
        }
    }

    return count;
}

int main()
{
    std::ifstream inf("A-small-attempt0.in");
    std::ofstream of("result.out");
    int T;
    inf >> T;
    int S = T;
    while (T > 0) {
        of << "Case #" << S - T + 1 << ": ";
        T--;

        std::string str;
        inf >> str;
        int n;
        inf >> n;

        A a(str, n);
        of << a.cal() << std::endl;
    }

    of.close();
    inf.close();

    return 0;
}
