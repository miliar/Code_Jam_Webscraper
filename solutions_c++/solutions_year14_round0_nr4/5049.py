#include<stdio.h>
#include<fstream>
#include<stdlib.h>
#include<algorithm>
#include<vector>
using namespace std;
vector<double> naomi,ken;
int cmpfun(const void *a,const void *b)
{
if (*(double *)a > *(double*)b)
return 1;
else if(*(double*)a < *(double*)b)
return -1;
else
return 0;
}
int findleastmax(double val)
{
int i;
for(i=0;i<ken.size();i++)
{
if(val<ken[i])
break;
}
return i;
}
int main()
{
int test_no=1,i,test,n;
ofstream myfile;
myfile.open ("example.txt");
double temp;
int wincheat,win;
scanf("%d",&test);
while(test_no<=test)
{
naomi.clear();
ken.clear();
scanf("%d",&n);
wincheat=0;
win=0;
for(i=0;i<n;i++)
{
scanf("%lf",&temp);
naomi.push_back(temp);
}
for(i=0;i<n;i++)
{
scanf("%lf",&temp);
ken.push_back(temp);
}
//qsort(naomi,n,sizeof(double),cmpfun);
sort(naomi.begin(),naomi.end());
/*printf("\n");
for(i=0;i<n;i++)
printf("%lf\t",naomi[i]);
for(i=0;i<n;i++)
printf("%lf\t",ken[i]);
printf("\n");*/
sort(ken.begin(),ken.end());
//printf("\n Sorted\n");
//qsort(ken,n,sizeof(double),cmpfun);
vector<double> kenc;
vector<double>naomic;
for(i=0;i<n;i++)
{
kenc.push_back(ken[i]);
naomic.push_back(naomi[i]);
}
//printf("\n done2\n");
//printf("\n");
/*for(i=0;i<n;i++)
printf("%lf\t",naomi[i]);
printf("\n");
for(i=0;i<n;i++)
printf("%lf\t",ken[i]);
printf("\n");*/
//printf("\n %d\n",naomi.begin());
if(naomi[0]>ken[n-1])
wincheat=n;
else if(naomi[n-1]<ken[0])
wincheat=0;
else
{
int ms=0;
for(int kl=0;kl<n;kl++)
{
if(naomi[kl]>ken[kl])
ms++;
}
if(ms==n)
{wincheat=n; }
else{
wincheat=n-1;
int conti=1;
int index2=0;
for(i=1;i<n;i++)
{
if(ken[index2]<naomi[i])
{
index2++;}
else{
//printf("%lf %lf\n",naomi[i],ken[index2]);
wincheat--;}
}
}
}
int head3=0,head1=n-1,head2=n-1;
for(i=0;i<n;i++)
{
int pos = findleastmax(naomi[head1]);
int size = (int ) ken.size();
if(pos>=size)
{
ken.erase(ken.begin());
win++;
}
else
ken.erase(ken.begin()+pos);
naomi.erase(naomi.begin()+naomi.size()-1);
head1--;
}
myfile<<"Case #"<<test_no<<": "<<wincheat<<" "<<win<<"\n";
test_no++;
}
myfile.close();
return 0;
}
