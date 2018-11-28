#include <iostream>
#include <vector>
#include <map>
#include<algorithm>
#include<string>
using namespace std;
void prob1 ()
{
    int T;
    cin >> T;
    string s;
    string res; //= "0";
    string tmp;// = "0";
    for (int c=1; c<=T; c++)
    {
        cin >> s;

        res = "0";
        tmp = "0";
        res[0] = s[0];
        int sz = s.size();
        for (int i=1; i<sz; i++){
            tmp[0] = s[i];
            if(s[i] >= res[0]){
                res = tmp + res;
            }
            else
                res = res + tmp;
        }

        cout << "Case #" << c << ": " <<  res << endl;
    }
}


void prob2 ()
{
    int T;
    cin >> T;

    for (int c= 1; c<=T; c++){
        int N;
        cin >> N;
        vector < vector <int > > v(2*N -1);

        for (int i=0; i<2*N -1; i++)
            v[i].resize(N);

        for (int i=0; i<2*N-1; i++)
            for (int j=0; j<N; j++)
                cin >> v[i][j];

        map <int, int> freq;

        for (int i=0; i< 2*N-1; i++)
            for (int j=0; j<N; j++)
                freq[v[i][j]]++;

        map <int, int> ::iterator it;

        vector <int> result;

        for (it = freq.begin(); it != freq.end(); it++){
            if (it->second %2 != 0)
                result.push_back(it->first);
        }

        sort(result.begin(), result.end());
        cout << "Case #" << c << ":";

        for (int i=0; i< result.size(); i++)
            cout << " " << result [i];

        cout << endl;

    }





}
void gen()
{
    for (int i=0; i<100; i++) {
        for (int j=0; j<500; j++)
            cout <<"AZ";
        cout << endl;
    }
}
using namespace std;

int main() {

    freopen("in.txt", "r", stdin);
    freopen ("out.txt", "w", stdout);
   // prob1();

    prob2();


   // gen();
    return 0;
}