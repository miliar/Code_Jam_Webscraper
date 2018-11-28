#include<iostream.h>
#include<conio.h>
#include<string.h>
#include<fstream.h>
void main()
{
	clrscr();
	int res1[150]={0};
    long n1,n2,T,m=0,n3,n4,n9=0;
    ifstream file("inp.in");
	file>>T;
    n9=T;
    while(T>0)
    {
	int count1=0,count2=0;
	int arr1[16]={0},l=0,l1=0,arr2[16]={0}, x1[4]={0}, x2[4]={0};
	file>>n1;
	for(int i=0;i<16;i++)
	{
	    file>>arr1[i];
	}
	file>>n2;
	for(int i1=0;i1<16;i1++)
	{
	    file>>arr2[i1];
	}
	T--;

    //COMPUTATIONAL PART STARTS
    while(n1>0){
    n1--;
    if(n1>0)
	count1=count1+4;
    }
    while(n2>0){
	n2--;
	if(n2>0)
	    count2=count2+4;
    }
    for(int j=count1;j<count1+4;j++)
    {
	x1[l]=arr1[j];
	l++;
    }

    for(int k=count2;k<count2+4;k++)
    {
	x2[l1]=arr2[k];
	l1++;
    }
    //COMPARISON WORK
    int temp=0,res=0;;
    for(int j1=0;j1<4;j1++){
    for(int j2=0;j2<4;j2++){
	if(x1[j1]==x2[j2]){
	    temp++;
	}
	if((temp==1)&&(x1[j1]==x2[j2]))
	{
	     res=x1[j1];
	}}
    }
    if(temp>1)
	res1[m]=1;
    if(temp==0)
	res1[m]=2;
    if(temp==1)
    {
	    res1[m]=3;
	    m++;
	    res1[m]=res;
    }
    m++;
    }
    ofstream file1("result.txt");
    int c=0;
    clrscr();
    for(int p=0;p<n9;p++)
    {
	c++;
	if(res1[p]==1)
	{
		file1<<"Case #"<<c<<": "<<"Bad magician!"<<endl;
	}
	if(res1[p]==2)
	{
		file1<<"Case #"<<c<<": "<<"Volunteer cheated!"<<endl;
	}
	if(res1[p]==3)
	{
	    p++;
	    n9++;
	    file1<<"Case #"<<c<<": "<<res1[p]<<endl;
	}
    }

getch();
}

