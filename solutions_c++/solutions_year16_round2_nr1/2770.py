#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#define all(a)                      a.begin(), a.end()
using namespace std;

string n;
int m[50];
int coun(string c)
{
    char a=c[0];
    int o=0;
    for(int i=0;i<n.size();i++)if(n[i]==a)o++;
    return o;
}

void take(int q,string b)
{

    for(int i=0;i<b.size();i++)
    {
        for(int p=0;p<q;p++){

        m[b[i]-65]--;
        }
    }
}

int main()
{
    int t;
    ifstream in("in.txt");
    ofstream out("out.txt");
    in>>t;

    for(int i=0;i<t;i++)
    {
        in>>n;
        vector<int> ats;
        for(int i = 0; i<27; i++)
    {
      m[i] = count(all(n), 'A'+i);
    }
        if(m['X'-65]>0){for(int i=0;i<m['X'-65];i++)ats.push_back(6);take(m['X'-65],"SIX");}//cout<<n<<endl;
        if(m['S'-65]>0){for(int i=0;i<m['S'-65];i++)ats.push_back(7);take(m['S'-65],"SEVEN");}//cout<<n<<endl;
        if(m['V'-65]>0){for(int i=0;i<m['V'-65];i++)ats.push_back(5);take(m['V'-65],"FIVE");}//cout<<n<<endl;
        if(m['F'-65]>0){for(int i=0;i<m['F'-65];i++)ats.push_back(4);take(m['F'-65],"FOUR");}//cout<<n<<endl;
        if(m['Z'-65]>0){for(int i=0;i<m['Z'-65];i++)ats.push_back(0);take(m['Z'-65],"ZERO");}//cout<<n<<endl;
        if(m['R'-65]>0){for(int i=0;i<m['R'-65];i++)ats.push_back(3);take(m['R'-65],"THREE");}//cout<<n<<endl;
        if(m['G'-65]>0){for(int i=0;i<m['G'-65];i++)ats.push_back(8);take(m['G'-65],"EIGHT");}//cout<<n<<endl;
        if(m['I'-65]>0){for(int i=0;i<m['I'-65];i++)ats.push_back(9);take(m['I'-65],"NINE");}//cout<<n<<endl;
        if(m['W'-65]>0){for(int i=0;i<m['W'-65];i++)ats.push_back(2);take(m['W'-65],"TWO");}//cout<<n<<endl;
        if(m['O'-65]>0){for(int i=0;i<m['O'-65];i++)ats.push_back(1);take(m['O'-65],"ONE");}//cout<<n<<endl;
sort(ats.begin(),ats.end());
        out<<"Case #"<<i+1<<": ";
        for(int i=0;i<ats.size();i++)out<<ats[i];out<<endl;
        n.clear();
        ats.clear();
        for(int p=0;p<49;p++)m[p]=0;
    }


    return 0;
}
