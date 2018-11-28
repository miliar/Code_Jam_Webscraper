#include <fstream>
#include <string>
#include <cmath>

using namespace std;

    ifstream cin ("1.in");
    ofstream cout ("output");
string reverse(string s)
{
    string ss="";
    for (int i=0; i<s.size(); ++i)
        ss+=s[s.size()-1-i];
    return ss;
}

bool isPalindrome(int n)
{
    string s="";
    while (n>0)
    {
        s+=(n%10+'0');
        n/=10;
    }
    if (s==reverse(s))
        return 1;
    else
        return 0;

}

int main()
{
    //cout << isPalindrome(1221) << "#";
    int n;
    cin >> n;
    for (int i=0; i<n; ++i)
    {
        int a,b;
        int s=0;
        cin >> a >> b;
        int x=(int)sqrt(a)-1;
        int y=(int)sqrt(b)+1;
        for (int j=x; j<=y; ++j)
        {
            if (a<=j*j && j*j<=b && isPalindrome(j*j) && isPalindrome(j))
            {

                s++;
            }
        }
        cout << "Case #" << i+1 << ": " << s << endl;


     }

    return 0;
}
