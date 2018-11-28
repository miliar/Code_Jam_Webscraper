#include <bits/stdc++.h>
using namespace std;


bool dofind(string cntr, string cntd)
{
    if (cntr.size() == 0)
        return false;
    for (int i = 0 ; i < cntd.size(); i++)
               if (cntr.find(cntd[i]) == string::npos)
               return false;
    return true;
}

// Check if s contains first element of the vector
/// If yes remove this element
int main()
{
   int tc;
freopen("k.in", "r", stdin);
freopen("b.out", "w+", stdout);
cin >> tc;
for (int i = 1; i <= tc ; i++)
{
   const char* args[] = {"ZERO", "TWO", "FOUR", "SIX", "EIGHT"};
    const char* args1[] = {"ONE", "THREE", "FIVE", "SEVEN", "NINE"};
    string str,strf;
    map<int, int> mp;
vector <string> vecE(args, args + 5);
vector <string> vecO(args1, args1 + 5);
cin >> str;
// Loop through strings
for (int j = 0 ; j < vecE.size() ; j++)
{
    while (dofind(str, vecE[j]))
    {
     // Remove characters from the string
     mp[j*2]++;
     for (int k = 0 ; k < vecE[j].size(); k++)
     {
         str.erase(std::find(str.begin(), str.end(), vecE[j][k]));

     }

    }
       }

       for (int j = 0 ; j < vecO.size() ; j++)
{
    while (dofind(str, vecO[j]))
    {
     // Remove characters from the string
     mp[(j*2) + 1]++;
     for (int k = 0 ; k < vecO[j].size(); k++)
     {
         str.erase(std::find(str.begin(), str.end(), vecO[j][k]));

     }

    }
       }

       for (int u = 0; u <= 9 ; u++)
       {
           //cout << mp[u] << "X";
           if (mp[u] != 0){
               // cout << "mpu=" << mp[u] << ":u=" << u << endl;
             for (int k = 0; k < mp[u]; k++)
             {

stringstream ss;
ss << u;
strf += ss.str();

             }

           }

       }

cout << "Case #" << i << ": " << strf << endl;
}

    return 0;
}
