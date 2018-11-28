#include<iostream.h>
#include<fstream.h>
#include<stdio.h>
#include<conio.h>
void main()
{
	int n,i,t=0,k,j,m=0,p=0,b[10];
	long long int a,z=0,ans;
	ofstream myfile;    	 //	FILE *fp;
	clrscr();
	myfile.open("output.out");		 //	fp=fopen("output.out","a");
	 freopen("input.in","r",stdin);
	//scanf("%d",&n);
	cin>>n;

	for(i=0;i<n;i++)
	{
       //	scanf("%ld",&a);
	 cin>>a;
	 if(a==0)
	 {printf("Case #%d: INSOMNIA\n",i+1);
	  myfile<<"Case #"<<i+1<<": INSOMNIA\n";	//fprintf(fp,"Case #%d: INSOMNIA\n",i+1);
	 goto me;}
	 for(j=1;j;j++)
	 {
	   z=a*j;  ans=z;
	   for(;z;z=z/10)
	   {
		t=z%10;
		for(k=0;k<m;k++)
		{
		    if(b[k]==t)
		    {p=1;}
		}
		if(p!=1)
		{b[k]=t;m++;}
		p=0;
		if(m==10)
		{ //printf("Case #%d: %d\n",i+1,ans);
		cout<<"Case #"<<i+1<<": "<<ans<<"\n";
		myfile<<"Case #"<<i+1<<": "<<ans<<"\n";	 //  fprintf(fp,"Case #%d: %ld\n",i+1,ans);

		goto me;}

	   }
	 }me:m=0;z=0;p=0;t=0;
	}myfile.close();	 //fclose(fp);
	 getch();

}