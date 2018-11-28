#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include<math.h>
using namespace std;
void remove_c(char *a,char c){
    for(int i=0;a[i];i++){
            if(a[i]==c){
                a[i]='a';
                return;
            }
        }
}
void remove_num(char *a,int num){
    switch(num){
    case 0:
        remove_c(a,'Z');
        remove_c(a,'E');
        remove_c(a,'R');
        remove_c(a,'O');
        break;
    case 1:
        remove_c(a,'O');
        remove_c(a,'N');
        remove_c(a,'E');
        break;
    case 2:
        remove_c(a,'T');
        remove_c(a,'W');
        remove_c(a,'O');
        break;
    case 3:
        remove_c(a,'T');
        remove_c(a,'H');
        remove_c(a,'R');
        remove_c(a,'E');
        remove_c(a,'E');
        break;
    case 4:
        remove_c(a,'F');
        remove_c(a,'O');
        remove_c(a,'U');
        remove_c(a,'R');
        remove_c(a,'E');
        break;
    case 5:
        remove_c(a,'F');
        remove_c(a,'I');
        remove_c(a,'V');
        remove_c(a,'E');
         break;
    case 6:
        remove_c(a,'S');
        remove_c(a,'I');
        remove_c(a,'X');
        break;
    case 7:
        remove_c(a,'S');
        remove_c(a,'E');
        remove_c(a,'V');
        remove_c(a,'E');
        remove_c(a,'N');
    break;
    case 8:
        remove_c(a,'E');
        remove_c(a,'I');
        remove_c(a,'G');
        remove_c(a,'H');
        remove_c(a,'T');
        break;
    case 9:
        remove_c(a,'N');
        remove_c(a,'I');
        remove_c(a,'N');
        remove_c(a,'E');
        break;


    }

}
int number(char *a,char c,int num){
    int temp=0;
    for(int i=0;a[i]!='\0';i++){
            if(a[i]==c){
                temp++;
                remove_num(a,num);
            }
        }

        return temp;
}
int main()
{
    FILE *fin = freopen("A-large.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("B12.out", "w", stdout);
    int b[10],t,n,j,temp;
    char a[2501];
    cin>>t;
    for(int k=1;k<=t;k++){
        for(int i=0;i<2000;i++)
            a[i]='0';
        for(int j=0;j<10;j++)
            a[j]='0';
        cin>>a;
        b[0]=number(a,'Z',0);
        b[2]=number(a,'W',2);
        b[8]=number(a,'G',8);
        b[4]=number(a,'U',4);
        b[6]=number(a,'X',6);
        b[1]=number(a,'O',1);
        b[3]=number(a,'H',3);
        b[5]=number(a,'F',5);
        b[7]=number(a,'V',7);
        b[9]=number(a,'I',9);
        cout << "Case #"<< k << ": ";
        for(int i=0;i<10;i++){
            for(int ho=0;ho<b[i];ho++)
                cout<<i;

        }
            cout<<endl;

    }

	return 0;
}
