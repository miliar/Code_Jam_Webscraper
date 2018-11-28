#include<iostream>
#include<iomanip>
#include<fstream>
#include<vector>
#include<algorithm>
using namespace std;


const int limit = 26;
const int oneAllowed = 3;
const int oneAllowed2 = 1;

vector<string> fairbases;
int lengthTarget;
string suffix;
int numOfOne;
bool even;

string make2String(int l)
{
    string str = "2";
    for (int i=0; i<l; i++)
        str.push_back('0');

    return str;
}

string makePalindrome(const string& input, const string& middle)
{
    string str;
    for (int i=input.length()-1; i>=0; i--)
        str.push_back(input[i]);

    str = input + middle + str;

    int n=str.length();
    int n2 = 2*n-1;
    string str2;
    for (int s=0; s<n2; s++) {
        int sum = 0;
        int bound = min(n-1, s);
        for (int i=max(s-n+1, 0); i<=bound; i++) {
            sum += (str[i]-'0') * (str[s-i]-'0');
        }
        str2.push_back(char(sum+'0'));
    }

    return str2;
}

void reset(int l, bool isEven)
{
    even = isEven;
    lengthTarget = l;
    suffix ="";
    numOfOne = 0;
}

void buildPalindrome()
{
    string now("1");
    now += suffix;
    if (even) {
        fairbases.push_back(makePalindrome(now, ""));
    }
    else {
        string now("1");
        now += suffix;
        fairbases.push_back(makePalindrome(now, "0"));
        fairbases.push_back(makePalindrome(now, "1"));
        if (numOfOne <= oneAllowed2) {
            fairbases.push_back(makePalindrome(now, "2"));
        }
    }
}

void buildSuffix()
{
    if (suffix.length() == lengthTarget) {
        buildPalindrome();
        return;
    }

    suffix.push_back('0');
    buildSuffix();
    suffix.erase(suffix.length()-1);

    if (numOfOne < oneAllowed) {
        suffix.push_back('1');
        numOfOne++;
        buildSuffix();
        suffix.erase(suffix.length()-1);
        numOfOne--;
    }
}

    
void buildFairBaseVec()
{
    fairbases.clear();
    
    fairbases.push_back("1");
    fairbases.push_back("4");
    fairbases.push_back("9");

    for(int k=1; k<=limit; k++) {
        reset(k-1, true);
        buildSuffix();
        string second = make2String(k-1);
        fairbases.push_back(makePalindrome(second, ""));

        if (k==limit)
            break;

        reset(k-1, false);
        buildSuffix();
        fairbases.push_back(makePalindrome(second, "0"));
        fairbases.push_back(makePalindrome(second, "1"));
    }
}

bool comp(const string& str1, const string& str2)
{
    if (str1.length()==str2.length())
        return str1 < str2;
    else
        return str1.length() < str2.length();
}

    
int main(){

    ifstream infile("file.in");
    ofstream outfile("file.out");

    int T;
    infile>>T;

    buildFairBaseVec();

    for (int t=0; t<T; t++){
        string l;
        string h;
        infile>>l>>h;

        vector<string>::iterator low = lower_bound(fairbases.begin(), fairbases.end(), l, comp);
        vector<string>::iterator high = upper_bound(fairbases.begin(), fairbases.end(), h, comp);

        outfile<<"Case #"<<t+1<<": "<<high-low<<endl;
    }

}
    
