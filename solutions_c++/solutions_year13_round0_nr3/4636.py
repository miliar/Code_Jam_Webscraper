#include<iostream>
#include<stdio.h>
#include<stdlib.h>
using namespace std;
int main(){
    int t;
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    cin >> t;
    int i;
    for(i=0;i<t;i++){
        int a, b;
        cin>>a>>b;
        int up, down;
        if(a<=1) up = 5;
        else if(a>1&&a<=4) up = 4;
        else if(a>4 && a<=9) up = 3;
        else if(a>9 && a<=121) up = 2;
        else if(a>121 && a<=484) up = 1;
        else up = 0;
        if(b>=484) down = 0;
        else if(b>=121 && b<484) down = 1;
        else if(b>=9 && b<121) down = 2;
        else if(b>=4 && b<9) down = 3;
        else if(b>=1 && b<4) down = 4;
        cout << "Case #"<<i+1<<": "<<up-down<<endl;
    }
    return 0;
}
