#include <iostream>
#include <string>
#include <map>
#include <vector>
using namespace std;

void stringPutToMap(const string& mvS, int removeCharMap[])
{
    for(int i = 0; i< mvS.length(); ++i)
    {
        ++removeCharMap[mvS[i]-'A'];
    }
}
bool removeChar(char c, int removeCharMap[])
{
    if(removeCharMap[c-'A']==0) return false;
    --removeCharMap[c-'A'];
    return true;
}
string getResult(const string& S)
{    
    int removeCharMap[26]={0};
    int num[10] = {0};
    bool processed[2000] = {0};
    int resultTimes[10] = {0};
    for(int i=0; i< S.length(); ++i)
    {
        if(removeChar(S[i], removeCharMap))
        {
            processed[i] = true;
            continue;
        }
        if(S[i] == 'Z')
        {
            stringPutToMap("ERO", removeCharMap);
            ++resultTimes[0];
        }
        else if(S[i] == 'W')
        {
            stringPutToMap("TO", removeCharMap);
            ++resultTimes[2];
        }
        else if(S[i] == 'U')
        {
            stringPutToMap("FOR", removeCharMap);
            ++resultTimes[4];
        }
        else if(S[i] == 'X')
        {
            stringPutToMap("SI", removeCharMap);
            ++resultTimes[6];
        }
        else if(S[i] == 'G')
        {
            stringPutToMap("EIHT", removeCharMap);
            ++resultTimes[8];
        }
        else
        {
            continue;
        }
        processed[i] = true;
    }

    for(int i=0; i< S.length(); ++i)
    {
        if(processed[i]) continue;
        if(removeChar(S[i], removeCharMap))
        {
            processed[i] = true;
            continue;
        }
        if(S[i] == 'O')
        {
            stringPutToMap("NE", removeCharMap);
            ++resultTimes[1];
        }
        else if(S[i] == 'T')
        {
            stringPutToMap("HREE", removeCharMap);
            ++resultTimes[3];
        }
        else if(S[i] == 'F')
        {
            stringPutToMap("IVE", removeCharMap);
            ++resultTimes[5];
        }
        else if(S[i] == 'S')
        {
            stringPutToMap("EVEN", removeCharMap);
            ++resultTimes[7];
        }
        else
        {
            continue;
        }
        processed[i] = true;
    }
    for(int i=0; i< S.length(); ++i)
    {
        if(processed[i]) continue;
        if(removeChar(S[i], removeCharMap))
        {
            processed[i] = true;
            continue;
        }
        if(S[i] == 'N')
        {
            stringPutToMap("INE", removeCharMap);
            ++resultTimes[9];
        }
        else if(S[i] == 'I')
        {
            stringPutToMap("NNE", removeCharMap);
            ++resultTimes[9];
        }
        else if(S[i] == 'E')
        {
            stringPutToMap("NIN", removeCharMap);
            ++resultTimes[9];
        }
        else
        {
            //cout << "ERROR" << endl;
            continue;
        }
        processed[i] = true;
    }
    string result = "";
    for(int i=0; i<10; ++i)
    {
        for(int j=0; j<resultTimes[i]; ++j)
        {
            result.push_back('0'+i);
        }
    }
    return result;
}
int main(int argc, char* argv[])
{
    int T = 0;
    cin >> T;
    for(int i=1; i<=T ;++i)
    {
        string S;
        cin >> S;
        string nresult  = getResult(S);
        cout << "Case #" << i << ": " << nresult << endl;
    }
}
/*
Z = 0
ONE ?
W = 2
THREE = ?
U = 4
FIVE = ?
X = 6
SEVEN = ?
G = 8
NINE = ?

-------------------
O = 1
T = 3
F = 5
S = 7
-------------------
N 
*/