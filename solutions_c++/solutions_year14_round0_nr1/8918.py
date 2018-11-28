#include <iostream>
#include <vector>
#include <fstream>
using namespace std;
string str(int n)
{
    string str = "";
    while (n!=0)
    {
        str += '0' + n%10;
        n/=10;
    }
    string res = "";
    for (int i = str.length()-1;i>=0;i--)
        res += str[i];
    return res;
}
int main()
{
    //ifstream cin("a.in");
    //ofstream fout("a.txt");
    //fout<<"myfile";
    int t;
    cin>>t;
    vector <string> res;
    for (int T = 0; T < t; T++)
    {
        int n1,  n2, temp;
        vector <int> ar1, ar2;
        cin>>n1;
        n1--;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
            {
                cin>>temp;
                if (i == n1)
                    ar1.push_back(temp);
            }
        cin>>n2;
        n2--;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
            {
                cin>>temp;
                if (i == n2)
                    ar2.push_back(temp);
            }
        vector <int> match;
        for (int i = 0;i < ar1.size(); i++)
            for (int j = 0; j < ar2.size(); j++)
                if (ar1[i] == ar2[j])
                    match.push_back(ar1[i]);
        if (match.size() == 0)
            res.push_back("Case #" + str(T+1) + ": Volunteer cheated!");
            //cout<<"Case #"<<T+1<<": Volunteer cheated!\n";
        if (match.size() == 1)
            res.push_back("Case #" + str(T+1) + ": " + str(match[0]));
            //cout<<"Case #"<<T+1<<": "<<match[0]<<endl;
        if (match.size() > 1)
            res.push_back("Case #" + str(T+1) + ": Bad magician!");
            //cout<<"Case #"<<T+1<<": Bad magician!\n";
    }
    for (int i=0;i<res.size();i++)
        cout<<res[i]<<endl;
    return 0;
}
