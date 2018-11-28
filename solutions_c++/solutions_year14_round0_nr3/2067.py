#include<stdlib.h>
#include<stdio.h>
#include<math.h>
#include<string.h>
const int N=20+5;
const double eps=1e-6;
int calable(double a,double b,int op){
return !((fabs(b)<eps)&&(op==3));
}
double cal(double a,double b,int op){
    double c=0;
    switch(op){
        case 0:c=a+b;break;
        case 1:c=a-b;break;
        case 2:c=a*b;break;
        case 3:c=a/b;break;
        default:break;
    }
    return c;
}

int checkexpression(double a,double b,double c,double d,int i,int j,int k,int type){
//a (i) b (j) c (k) d
switch(type){
case 0:
if(!calable(b,c,j))return 0;
      b=cal(b,c,j);
if(!calable(a,b,i))return 0;
      a=cal(a,b,i);
if(!calable(a,d,k))return 0;
      a=cal(a,d,k);
return fabs(a-24)<eps;break;

case 1:
if(!calable(a,b,i))return 0;
      a=cal(a,b,i);
if(!calable(a,c,j))return 0;
      a=cal(a,c,j);
if(!calable(a,d,k))return 0;
      a=cal(a,d,k);
return fabs(a-24)<eps;break;

case 2:
if(!calable(a,b,i))return 0;
      a=cal(a,b,i);
if(!calable(c,d,k))return 0;
      c=cal(c,d,k);
if(!calable(a,c,j))return 0;
      a=cal(a,c,j);
return fabs(a-24)<eps;break;

case 3:
if(!calable(c,d,k))return 0;
      c=cal(c,d,k);
if(!calable(b,c,j))return 0;
      b=cal(b,c,j);
if(!calable(a,b,i))return 0;
      a=cal(a,b,i);
return fabs(a-24)<eps;break;

case 4:
if(!calable(b,c,j))return 0;
      b=cal(b,c,j);
if(!calable(b,d,k))return 0;
      b=cal(b,d,k);
if(!calable(a,b,i))return 0;
      a=cal(a,b,i);
return fabs(a-24)<eps;break;

}

}
int check(int a,int b,int c,int d){
int i,j,k,t;
for(i=0;i<4;i++)
for(j=0;j<4;j++)
for(k=0;k<4;k++)
for(t=0;t<5;t++)
if(checkexpression((double)a,(double)b,(double)c,(double)d,i,j,k,t))return 1;
return 0;
}

int recursive(int num[],int i,int n){
int j,tmp;
if(i>=n){
if(check(num[0],num[1],num[2],num[3]))return 1;
else return 0;
}
for(j=i;j<n;j++){
    tmp=num[j];num[j]=num[i];num[i]=tmp;
    if(recursive(num,i+1,n))return 1;
    tmp=num[j];num[j]=num[i];num[i]=tmp;
}
return 0;
}

//4个数据的范围1-13
//a,b,c,d如果可以组成24点，can24返回1，不能则can24返回0
//（此外，你可以在can24内调用你写的另外一个函数）
int can24(int a, int b, int c, int d)
{
int num[4];
num[0]=a;
num[1]=b;
num[2]=c;
num[3]=d;
if(recursive(num,0,4))return 1;
else return 0;
}    
//start 提示：自动阅卷起始唯一标识，请勿删除或增加。
//可不完成，完成功能函数即可，给定主函数，是为方便你测试
int main(){
    printf("%d\n",can24(1,1,1,10));
    printf("%d\n",can24(6,6,6,6));
    printf("%d\n",can24(5,5,5,1));
    printf("%d\n",can24(1,1,1,11));


        //
    return 0;
}
//end //提示：自动阅卷结束唯一标识，请勿删除或增加。
