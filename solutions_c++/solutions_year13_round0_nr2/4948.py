#include <iostream>
#include <vector>
using namespace std;

int a,b,c,d,e,f;

int main(){
        int t;
        cin >> t;
        for(int cse = 1; cse <= t; cse++){
                int n,m;
                cin >> n >> m;
                int pat[110][110]= {0};
                int cur[110][110] = { 0};
                int set[110][110] = {0};

                for(int i = 0; i < n; i++)
                        for(int j = 0; j < m; j++){
                                cin >> pat[i][j];
                        }

                for(int i = 0; i < n; i++){
                        int max = 0;
                        for(int j = 0; j < m; j++)
                                if (pat[i][j] > max)
                                        max = pat[i][j];
                        for(int j = 0; j < m; j++){
                                cur[i][j] = max;
                                if (cur[i][j] == pat[i][j])
                                        set[i][j] = 1;
                        }
                }

                for(int j = 0; j < m; j++){
                        int max = 0;
                        for(int i = 0; i < n; i++)
                                if (pat[i][j] > max)
                                        max = pat[i][j];
                        for(int i = 0; i < n; i++){
                                if (cur[i][j] > max)
                                        cur[i][j] = max;
                                if (cur[i][j] == pat[i][j])
                                        set[i][j] = 1;
                        }
                        //    cout << max << endl;
                }

                int flag = 1;
                for(int i = 0; i < n; i++){
                        for(int j = 0; j < m; j++)
                                flag = flag && set[i][j];
                }

                if (flag){
                        cout << "Case #" << cse << ": YES"<< endl;
                }
                else{
                        cout << "Case #" << cse << ": NO"<< endl;
                }

                
        }

        return 0;
}
                        
                        
                                        
                                


                
