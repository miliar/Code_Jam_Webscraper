#include<cstdio>
#include<iostream>
#define gc getchar_unlocked
using namespace std;
void inline scanint(int &x)
{
    register int c = gc();
    x = 0;
    int neg = 0;
    for(;((c<48 || c>57) && c != '-');c = gc());
    if(c=='-') {neg=1;c=gc();}
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
    if(neg) x=-x;
}
int main(){
	int arr[4][4];
	int *rowarr=new int[4];
	int flag=0;
	int count=0,t=0;
	char c[]="Case #";
	char c1[]="Bad magician!";
	char c2[]="Volunteer cheated!";
	int number=0;
	int caseno=1;
	int row1=0,row2=0;
	scanint(t);
	while(t--){
	scanint(row1);
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++)
			scanint(arr[i][j]);
		}
	for(int i=0;i<4;i++)
	rowarr[i]=arr[row1-1][i];
		scanint(row2);
		for(int i=0;i<4;i++){
		for(int j=0;j<4;j++)
			scanint(arr[i][j]);
		}
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
		if(arr[row2-1][j]==rowarr[i]){
			number=rowarr[i];
			count++;
		}
			if(count>=2)
			{
				flag=1;
				break;
			}
	}
	if(flag==1)
	break;
	}
	if(count==0)
	printf("%s%d%s %s",c,caseno,":",c2);
	else if(flag==1)
	printf("%s%d%s %s",c,caseno,":",c1);
	else 
	printf("%s%d%s %d",c,caseno,":",number);
	printf("%s","\n");
	count=0;
	number=0;
	caseno++;
	flag=0;
	}
	return 0;
}
