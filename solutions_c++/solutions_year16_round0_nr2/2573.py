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

int transition(string s){
    int answer=0;
    for(int i=1; i<s.length(); i++){
        if(s[i]!=s[i-1]) answer++;
    }
    return answer;
}

int main(){
    std::ios::sync_with_stdio(false);
    #ifdef FILE
		FILE;
	#endif

    int t,answer;
    string s;
    cin>>t;

    for(int i=0; i<t; i++){
        cin>>s;
        int d= transition(s)+1;
        if(d%2!=0){
            //odd
            if(s[0]=='+' && s[s.length()-1]=='+') answer=d-1;
            else if(s[0]=='-' && s[s.length()-1]=='-') answer=d;
        }
        else if(d%2==0){
            //even
            if(s[0]=='+' && s[s.length()-1]=='-') answer=d;
            else if(s[0]=='-' && s[s.length()-1]=='+') answer=d-1;
        }
        cout<<"Case #"<<i+1<<": "<<answer<<endl;
    }

    #ifdef TIMER
		TIMER;
	#endif
    return 0;
}

/*****************************************************************************************************
                                                                                     ,----,.
                                                                                   ,'   ,' |
      ,-.                                              ,--,        ,----..       ,'   .'   |
  ,--/ /|                                            ,--.'|       /   /   \    ,----.'    .'
,--. :/ |           ,--,        ,---,                |  | :      /   .     :   |    |   .'
:  : ' /          ,'_ /|    ,-+-. /  |               :  : '     .   /   ;.  \  :    :  |--,
|  '  /      .--. |  | :   ,--.'|'   |    ,--.--.    |  ' |    .   ;   /  ` ;  :    |  ;.' \
'  |  :    ,'_ /| :  . |  |   |  ,"' |   /       \   '  | |    ;   |  ; \ ; |  |    |      |
|  |   \   |  ' | |  . .  |   | /  | |  .--.  .-. |  |  | :    |   :  | ; | '  `----'.'\   ;
'  : |. \  |  | ' |  | |  |   | |  | |   \__\/: . .  '  : |__  .   |  ' ' ' :    __  \  .  |
|  | ' \ \ :  | : ;  ; |  |   | |  |/    ," .--.; |  |  | '.'| '   ;  \; /  |  /   /\/  /  :
'  : |--'  '  :  `--'   \ |   | |--'    /  /  ,.  |  ;  :    ;  \   \  ',  /  / ,,/  ',-   .
;  |,'     :  ,      .-./ |   |/       ;  :   .'   \ |  ,   /    ;   :    /   \ ''\       ;
'--'        `--`----'     '---'        |  ,     .-./  ---`-'      \   \ .'     \   \    .'
                                        `--`---'                   `---`        `--`-,-'


 *****************************************************************************************************/
