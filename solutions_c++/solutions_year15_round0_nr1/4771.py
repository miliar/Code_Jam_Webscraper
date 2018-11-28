#include<iostream>
#include<fstream>
using namespace std;

int main()
{
        fstream fin;
        fstream fout;
        fin.open("A-small-attempt1.in",ios::in);   
        fout.open("1.text",ios::out);
    int T,N = 1;
    fin >> T;
    
    while(T--)
    {

        int MAX,ans =0 ,IS[1010];
        string S;
        fin >> MAX;
        fin >> S;
        for(int i = 0; i <= MAX;i++)IS[i] = S[i] - '0';
        int now = IS[0];
        if(MAX  == 0)ans = 0;
        else {
              
            for(int i = 1; i <= MAX; i++)
            {
                    if(i > now && IS[i] > 0){
                            ans += (i - now);
                            now += (IS[i] + ans);
                    }
                    else now += IS[i];
            }       
        }
        fout << "Case #" << N++ << ": " << ans << endl;
    }
    
    
    system("pause");
    
}
