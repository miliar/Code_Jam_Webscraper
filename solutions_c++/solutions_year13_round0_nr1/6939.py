#include<iostream>
using namespace std;
int main(){
int n,x1=0,o1=0,t1=0,d1=0,x2=0,o2=0,t2=0,d2=0,f=0,x3=0,o3=0,t3=0,x4=0,o4=0,t4=0;
int xw=0,ow=0,nc=0;
char a[4][4];
cin>>n;
int b[n];
for(int i=0;i<n;i++){
    for(int j=0;j<4;j++)
        cin>>a[j];
    for(int j=0;j<4;j++){
    x1=0,o1=0,d1=0,x2=0,o2=0,d2=0,t1=0,t2=0,x3=0,o3=0,t3=0,x4=0,t4=0,o4=0;
        for(int k=0;k<4;k++){
            switch(a[j][k]){
                case 'X':x1++;break;
                case 'O':o1++;break;
                case 'T':t1++;break;
                case '.':d1++;break;
            }
            switch(a[k][j]){
                case 'X':x2++;break;
                case 'O':o2++;break;
                case 'T':t2++;break;
                case '.':d2++;break;
            }
        }
        if((x1==4||(x1==3&&t1==1))||(x2==4||(x2==3&&t2==1))) {xw=1;break;}
        else if(o1==4||(o1==3&&t1==1)||(o2==4||(o2==3&&t2==1))){ow=1;break;}
        else if(d1!=0||d2!=0) nc=1;
        
    }
    for(int y=0;y<4;y++){
        switch(a[y][y]){
        case 'X': x3++;break;
        case 'T':t3++;break;
        case 'O':o3++;
        }
        }
        if((x3==3&&t3==1)||x3==4) xw=1;
        else if((o3==3&&t3==1)||o3==4) ow=1;
    for(int y=0;y<4;y++){
        switch(a[y][3-y]){
        case 'X': x4++;break;
        case 'T':t4++;break;
        case 'O':o4++;    
        }
    }
    if((x4==3&&t4==1)||x4==4) xw=1;
    else if((o4==3&&t4==1)||o4==4) ow=1;
    if(xw==1) b[f++]=0;
    else if(ow==1) b[f++]=1;
    else if(nc==1) b[f++]=2;
    else b[f++]=3;
    cin.get();
    xw=0,ow=0,nc=0;
}
for(int z=0;z<n;z++){
cout<<"Case #"<<z+1<<": ";
switch(b[z]){
case 0:cout<<"X won\n";break;
case 1:cout<<"O won\n";break;
case 2:cout<<"Game has not completed\n";break;
case 3:cout<<"Draw\n";break;
}
}
return 0;
}
