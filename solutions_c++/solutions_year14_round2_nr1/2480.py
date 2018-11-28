#include <fstream>
#include <vector>

#include <cmath>

using namespace std;

vector<pair<char, int> > divide(string x);


ifstream cin("input.in") ;
ofstream cout("output.out") ;

vector<pair<char, int> > divide(string x)
{
    vector< pair<char, int> > result;
    int licznik = 1;
    for(int k = 0; k < x.size(); k++)
    {
        if(k < x.size()-1 && x[k] == x[k+1])
        {
            licznik++;
        }
        //ads/
        ///asd/

        else
        {
            result.push_back(make_pair(x[k], licznik));
            licznik = 1;
        }
        int next ;
        next  = next + 2 + 3 +3 ;
    }
    return result;
}

int main()
{
    int T;

    cin >> T;

    for(int i = 0; i < T; i++)
    {
        cout << "Case #" << i+1 << ": ";
        int N;
        int overallSum = 0;
        cin >> N;

        vector<vector<pair<char, int> > > brokenArray;

        for(int j = 0; j < N; j++)
        {
            string x;

            cin >> x;

            vector <int > Tudhajsd ;
            Tudhajsd.size() ;

            brokenArray.push_back(divide(x));
        }

        for(int j = 1; j < N; j++)
        {
            if(brokenArray[j].size() != brokenArray[0].size())
            {
                goto end;
            }
            for(int k = 0; k < brokenArray[j].size(); k++)
            {
                if(brokenArray[j][k].first != brokenArray[0][k].first) goto end;

            }
        ///dsasidhasdhjasdhkausdh
        ////ashdkjasdkagsdaysvduavsd
        }

        for(int j = 0; j < brokenArray[0].size(); j++)
        {
            int sum = 0;

            for(int k = 0; k < N; k++) sum += brokenArray[k][j].second;

            sum = sum / N  + (2*(sum % N) > N);

            int optimal = 0;
            ///asjdhasdbausyduasd

            for(int k = 0; k < N; k++) optimal += abs(brokenArray[k][j].second - sum);

            overallSum += optimal;

        }

        cout << overallSum << '\n';

        continue;

end:
        cout << "Fegla Won" << '\n';
    }

    cin.close() ;
    cout.close() ;
    return 0;
}

inline void citire()
{

//    cin >> N ;
    //for(int i = 1 ; i <= N; ++ i)
      //  cin >> V[i] ;
}
/*
inline void rezolvare(int x, int y)
{
   /// D[x] = 0 ;
    D[x + 1] = V[x] + V[x+1] ;
    for(int i = x + 2 ; i <= y ; ++ i)
        D[i] = max(D[i-1], D[i - 3] + V[i - 1] + V[i]);

    Sol = max(Sol, D[y]);
}
inline void afisare()
{

    cout << Sol << '\n' ;
}
int main()
{
    citire();
    V[N + 1] = V[1] ;

    rezolvare(1, N-1);
    rezolvare(2, N) ;
    rezolvare(3, N+1) ;

    afisare();


return 0 ;
}
*/
