#include <iostream>
#include <string>
using namespace std;

int T, N;
int P[28];
string ans;

int main(){

    scanf("%d",&T);
    for (int i=1; i <= T; i++){

        ans.clear();
        cin >> N;

        //For 2 parties
        if (N==2){
            cin >> P[1] >> P[2];
            if (P[1] == P[2]){
                while(P[1]--){
                    ans.append("AB ");
                }
            }
            else if (P[1] > P[2]){
                while (P[1] > P[2]){
                    ans.append("A ");
                    P[1]--;
                }
                while (P[1]--){
                    ans.append("AB ");
                }
            }
            else{
                while (P[2] > P[1]){
                    ans.append("B ");
                    P[2]--;
                }
                while (P[2]--){
                    ans.append("AB ");
                }
            }
        }

        //For 3 parties
        else{
            cin >> P[1] >> P[2] >> P[3];
            if (P[1] >= P[2] && P[1] >= P[3]){
               if (P[2] > P[3]){
                    while (P[1] > P[2]){
                        ans.append("A ");
                        P[1]--;
                    }
                    while (P[1] > P[3]){
                        ans.append("AB ");
                        P[1]--;
                        P[2]--;
                    }
                    while (P[3] != 0){
                        ans.append("C ");
                        P[3]--;
                        ans.append("AB ");
                        P[1]--;
                        P[2]--;
                    }
               }
               else if (P[2] < P[3]){
                    while (P[1] > P[3]){
                        ans.append("A ");
                        P[1]--;
                    }
                    while (P[1] > P[2]){
                        ans.append("AC ");
                        P[1]--;
                        P[3]--;
                    }
                    while (P[2] != 0){
                        ans.append("B ");
                        P[2]--;
                        ans.append("AC ");
                        P[1]--;
                        P[3]--;
                    }
               }
               else{
                    if (P[1] == P[2]){
                        while(P[1] !=0){
                            ans.append("C ");
                            P[3]--;
                            ans.append("AB ");
                            P[1]--;
                        }
                    }
                    else{
                        while (P[1] > P[2]){
                            P[1]--;
                            ans.append("A ");
                        }
                        while (P[1] != 0){
                            ans.append("C ");
                            P[3]--;
                            ans.append("AB ");
                            P[1]--;
                        }
                    }
               }
            }
            else if (P[2] >= P[3] && P[2] >= P[1]){
               if (P[1] > P[3]){
                    while (P[2] > P[1]){
                        ans.append("B ");
                        P[2]--;
                    }
                    while (P[2] > P[3]){
                        ans.append("AB ");
                        P[2]--;
                        P[1]--;
                    }
                    while (P[3] != 0){
                        ans.append("C ");
                        P[3]--;
                        ans.append("AB ");
                        P[1]--;
                        P[2]--;
                    }
               }
               else if (P[1] < P[3]){
                    while (P[2] > P[3]){
                        ans.append("B ");
                        P[2]--;
                    }
                    while (P[2] > P[1]){
                        ans.append("BC ");
                        P[2]--;
                        P[3]--;
                    }
                    while (P[2] != 0){
                        ans.append("B ");
                        P[2]--;
                        ans.append("AC ");
                        P[1]--;
                        P[3]--;
                    }
               }
               else{
                    if (P[2] == P[3]){
                        while(P[2] != 0){
                            ans.append("B AC ");
                            P[2]--;
                        }
                    }
                    else{
                        while (P[2] > P[1]){
                            P[2]--;
                            ans.append("B ");
                        }
                        while (P[1] != 0){
                            ans.append("C ");
                            P[3]--;
                            ans.append("AB ");
                            P[1]--;
                        }
                    }
               }
            }
            else{
               if (P[1] > P[2]){
                    while (P[3] > P[1]){
                        ans.append("C ");
                        P[3]--;
                    }
                    while (P[3] > P[2]){
                        ans.append("AC ");
                        P[3]--;
                        P[1]--;
                    }
                    while (P[3] != 0){
                        ans.append("C ");
                        P[3]--;
                        ans.append("AB ");
                        P[1]--;
                        P[2]--;
                    }
               }
               else if (P[1] < P[2]){
                    while (P[3] > P[2]){
                        ans.append("C ");
                        P[3]--;
                    }
                    while (P[3] > P[1]){
                        ans.append("BC ");
                        P[2]--;
                        P[3]--;
                    }
                    while (P[2] != 0){
                        ans.append("B ");
                        P[2]--;
                        ans.append("AC ");
                        P[1]--;
                        P[3]--;
                    }
               }
               else{
                    if (P[3] == P[2]){
                        while(P[3] != 0){
                            ans.append("C AB");
                            P[3]--;
                        }
                    }
                    else{
                        while (P[3] > P[2]){
                            P[3]--;
                            ans.append("C ");
                        }
                        while (P[1] != 0){
                            ans.append("C ");
                            P[3]--;
                            ans.append("AB ");
                            P[1]--;
                        }
                    }
               }
            }
        }

        cout<<"Case #"<<i<<": "<<ans;
        if (i!=T)
            cout<<endl;
    }
    return 0;
}
