#include <bits/stdc++.h>
#define F first
#define S second
#define MOD 1000000007
#define PI 3.1415926535897932384626433832795
#define FILE freopen("test.in", "r", stdin); freopen("test.out", "w", stdout)
//#define TIMER cout<<endl<<"Time Taken : "<<(double)(clock()-t1)/CLOCKS_PER_SEC<<" seconds."<<endl
typedef long long ll;
clock_t t1 = clock();
using namespace std;

int main(){
    std::ios::sync_with_stdio(false);
    #ifdef FILE
		FILE;
	#endif
        int t;
        cin>>t;
        for(int i=1; i<=t; i++){
            string s,tt;
            cin>>s;
            char check=s[0];
            tt=check;
            for(int j=1; j<s.length(); j++){
                check=tt[0];
                if(s[j]>=check){
                    tt.insert(0,1,s[j]);
                }
                else tt.insert(j,1,s[j]);
            }

            cout<<"Case #"<<i<<": "<<tt<<endl;
        }
    #ifdef TIMER
		TIMER;
	#endif
    return 0;
}

/****************************************************************************************************
*                                                                                         ,----,.   *
*                                                                                       ,'   ,' |   *
*          ,-.                                              ,--,        ,----..       ,'   .'   |   *
*      ,--/ /|                                            ,--.'|       /   /   \    ,----.'    .'   *
*    ,--. :/ |           ,--,        ,---,                |  | :      /   .     :   |    |   .'     *
*    :  : ' /          ,'_ /|    ,-+-. /  |               :  : '     .   /   ;.  \  :    :  |--,    *
*    |  '  /      .--. |  | :   ,--.'|'   |    ,--.--.    |  ' |    .   ;   /  ` ;  :    |  ;.' \   *
*    '  |  :    ,'_ /| :  . |  |   |  ,"' |   /       \   '  | |    ;   |  ; \ ; |  |    |      |   *
*    |  |   \   |  ' | |  . .  |   | /  | |  .--.  .-. |  |  | :    |   :  | ; | '  `----'.'\   ;   *
*    '  : |. \  |  | ' |  | |  |   | |  | |   \__\/: . .  '  : |__  .   |  ' ' ' :    __  \  .  |   *
*    |  | ' \ \ :  | : ;  ; |  |   | |  |/    ," .--.; |  |  | '.'| '   ;  \; /  |  /   /\/  /  :   *
*    '  : |--'  '  :  `--'   \ |   | |--'    /  /  ,.  |  ;  :    ;  \   \  ',  /  / ,,/  ',-   .   *
*    ;  |,'     :  ,      .-./ |   |/       ;  :   .'   \ |  ,   /    ;   :    /   \ ''\       ;    *
*    '--'        `--`----'     '---'        |  ,     .-./  ---`-'      \   \ .'     \   \    .'     *
*                                            `--`---'                   `---`        `--`-,-'       *
*                                                                                                   *
*                                                                                                   *
****************************************************************************************************/
