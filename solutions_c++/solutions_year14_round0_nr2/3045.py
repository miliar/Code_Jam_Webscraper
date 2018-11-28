 #include<iostream>
 #include<cstdio>
 #include<cstdlib>
 #include<cstring>
 #include<cmath>
 #include<algorithm>
 #include<vector>
 #include<map>
 #include<utility>
 #define mod 1000000007
 using namespace std;
 int main(){
 freopen("input.txt","r",stdin);
 freopen("output.txt","w",stdout);
 int t,z=1;
 scanf("%d",&t);
 while(t--){
double c,f,x,insec=2,time=0,pt=99999999,timec=0,sec=2,ans=0.0;
int count=0;
int i;
scanf("%lf%lf%lf",&c,&f,&x);


for(i=0;;i++){
 
 time = x/insec + timec;
 timec = c/insec + timec;

 if(time>pt)
 break ;
 
 pt = time;
 insec = insec + f;
 count++;
 }

insec = insec - f;

for(i=0;i<count-1;i++){
ans = ans + c/sec;
sec = sec + f;
}   
ans = ans + x/(insec);
//printf("Case #%d: %lf\n",x,ans);x++;
printf("Case #%d: %.7lf\n",z++,ans); 
           }
//system("Pause");
return 0;
}
