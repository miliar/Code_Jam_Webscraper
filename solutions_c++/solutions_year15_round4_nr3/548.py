#include <iostream>
#include <vector>
#include <map>

using namespace std;

map < string, int > M; //slowu przyporzadkowywuje numer;
vector < vector < int > > V;
int liczba[10000];

int main()
{
    int te;
    cin>>te;
    for(int testy = 1; testy <= te; testy++)
    {
        M.clear();
        V.clear();
        V.resize(30000);
        int n, ileslow = 0;
        cin>>n;
        string s;
        getline(cin, s);
        for(int i=0; i<n; i++)
        {
            getline(cin, s);
            string akt = "";
            for(int j=0; j<s.size(); j++)
            {
                if (s[j] != ' ')
                    akt = akt + s[j];
                else
                {
                    if (M[akt]==0)
                    {
                        ileslow++;
                        M[akt] = ileslow; 
                    }
                    if ( V[ M[akt] ].size() == 0 || V[ M[akt] ][ V[ M[akt] ].size()-1 ] != i)
                        V[ M[akt] ].push_back(i);
                    akt = "";
                }
            }
            if (M[akt]==0)
            {
                ileslow++;
                M[akt] = ileslow; 
            }
            if ( V[ M[akt] ].size() == 0 || V[ M[akt] ][ V[ M[akt] ].size()-1 ] != i)
                    V[ M[akt] ].push_back(i);
            akt = "";
        }
        
        
  /*      for(int i=1; i<=ileslow; i++)
        {
            for(int j=0; j<V[i].size(); j++)
                cout<<V[i][j]<<" ";
            cout<<endl;
        }
    */   
        for(int i=1; i<=ileslow; i++)
        {
            liczba[i]=0;
            for(int j=0; j<V[i].size(); j++)
                liczba[i] += (1 << (V[i][j]) );
        //    cout<< liczba[i]<<" "<<( (liczba[i])&9)<<" ";//////////
        } 
      //  cout<<endl;
        int minimum = 1000000;
      //  cout << ileslow << endl;
     //   continue;
        for(int i=0; i< (1<<(n-2)); i++)
        {
            int akt = i * 4 + 1, ilezlych = 0;
            for(int j=1; j<=ileslow; j++)
            {
    //            if (akt == 9)
    //                cout << (liczba[j] & akt)<<" "<<liczba[j]<<"A";
                if ( (liczba[j] & akt)  != 0 && (liczba[j] & akt) != liczba[j])
                    ilezlych++;

            }
            minimum = min(minimum, ilezlych);
        }
        printf("Case #%d: %d\n", testy, minimum);
    }    
   // system("PAUSE");    
    return 0;
}
