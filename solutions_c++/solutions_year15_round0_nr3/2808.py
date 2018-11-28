#include <iostream>
#include <map>
#include <cmath>
#include <vector>

using namespace std;

static int T;

string mult(string as, string bs)
{
    string result;
    bool aminus, bminus, minus = false;
    
    aminus = as.length() > 1;
    bminus = bs.length() > 1;
    
    minus = (aminus && !bminus) || (!aminus && bminus);

    char a, b;
    a = (aminus)?as[1]:as[0];
    b = (bminus)?bs[1]:bs[0];

    if (a == '1') {
        if (b == '1')
            result = '1';
        else if (b == 'i')
            result = 'i';
        else if (b == 'j')
            result = 'j';
        else if (b == 'k')
            result = 'k';
    } else if (a == 'i') {
        if (b == '1')
            result = 'i';
        else if (b == 'i')
            result = "-1";
        else if (b == 'j')
            result = 'k';
        else if (b == 'k')
            result = "-j";
    } else if (a == 'j') {
        if (b == '1')
            result = 'j';
        else if (b == 'i')
            result = "-k";
        else if (b == 'j')
            result = "-1";
        else if (b == 'k')
            result = 'i';
    } else if (a == 'k') {
        if (b == '1')
            result = 'k';
        else if (b == 'i')
            result = 'j';
        else if (b == 'j')
            result = "-i";
        else if (b == 'k')
            result = "-1";
    }
    
    if (minus) {
        if (result.length() > 1)
            result = result[1];
        else
            result = "-" + result;
    }
    
    return result;
}

string mult(string as, char b)
{
    string bs(1, b);
    return mult(as, bs);
}

string mult(char a, string bs)
{
    string as(1, a);
    return mult(as, bs);
}

bool dijkstra(const string &str, int X)
{
    int N = str.length();
    int total_length = N*X;
    
    string chunk = "1";
    for (int i = 0; i < str.length(); ++i)
        chunk = mult(chunk, str[i]);
    
    vector<string> trois;
    trois.resize(N);
    string temp = "1";
    for (int i = N-1; i >= 0; --i)
    {
        temp = mult(str[i], temp);
        trois[i] = temp;
    }
    
    string first = "1";
    for (int i = 0; i <= 2*N - 2 && i < total_length - 2; ++i) {
        
        first = mult(first, str[i%N]);
        
        if (first == "i") {
            string second = "1";
            
            for (int j = i+1; j <= i+1 + 2*N-2 && j < total_length - 1; ++j) {
                
                second = mult(second, str[j%N]);
                
                if (second == "j") {

                    string third = "1";
                    
                    if ((j+1)%N != 0)
                        third = trois[(j+1)%N];
                
                    
                    int count = ceil((float)j/N);
                    
                    for (int x = count + 1; x <= X; ++x) {
                        third = mult(third, chunk);
                    }
                    
                    if (third == "k")
                    {
                        cerr << "found" << i << ";" << j << endl;
                        return true;
                    }
                }
            }
        }
    }
    
    return false;
}

bool dijkstra2(const string &str)
{
    int N = str.length();

    vector<string> trois;
    trois.resize(N);
    string temp = "1";
    for (int i = N-1; i >= 0; --i)
    {
        temp = mult(str[i], temp);
        trois[i] = temp;
    }
    
    string first = "1";
    for (int i = 0; i < N-2; ++i) {
        first = mult(first, str[i]);
        
       // cerr << i <<";" << first << endl;
        
        if (first == "i") {
            string second = "1";
            
            for (int j = i+1; j < N-1; ++j) {
                
                second = mult(second, str[j]);
                
                if (second == "j") {
                    
 
                        string third = trois[j+1];
                    
                        if (third == "k")
                            return true;
     
                }
            }
        }
    }
    
    return false;
}



int main(int argc, const char * argv[]) {
    
    cin >> T;
    cin.ignore();
    
    //cerr << T << endl;
    
    for (int i = 0; i < T; ++i)
    {
        int length, repetition;
        string value;
        cin >> length; cin.ignore();
        cin >> repetition; cin.ignore();
        cin >> value; cin.ignore();
        
        int total = length * repetition;
        string response, total_str;
        
        for (int i = 0; i < repetition; ++i)
            total_str += value;
        
        if (total < 3)
            response = "NO";
        else if (total == 3)
        {
            if (value != "ijk")
                response = "NO";
            else
                response = "YES";
        }
        else {
            string str;
            
            response = dijkstra2(total_str)?"YES":"NO";
        }
        
        cerr << "n°" << i << endl;
        cout << "Case #" << (i+1) << ": " << response << endl;
    }
    
    return 0;
}
