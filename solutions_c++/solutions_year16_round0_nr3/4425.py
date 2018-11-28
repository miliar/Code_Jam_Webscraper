#include<bits/stdc++.h>
typedef long long lld;
using namespace std;
lld decimal_binary(lld n)
{
    lld rem, i=1, binary=0;
    while (n!=0)
    {
        rem=n%2;
        n/=2;
        binary+=rem*i;
        i*=10;
    }
    return binary;
}
lld baseans(lld ar[],lld base,lld size)
{
	lld i=0,ans=0;
	for(i=0;i<size;i++)
	{
		ans+=(ar[i]*pow(base,i));
	}
	return ans;
}
lld isprime(lld num)
{
	int i;
	for(i=2;i*i<=num;i++)
	{
		if(num%i==0)
			return 0;
	}
	return 1;
}
int main()
{
	FILE *input,*output;
	lld t,i,j,m,a,b,tmp,tmp2,base2;
	input=fopen("new.txt","r");
	if(input==NULL)
	{
		printf("ERROR!!");
		exit(0);	
	}
	output=fopen("ect.txt","w");
	if(output==NULL)
	{
		printf("Error!!");
		exit(0);
	}
	fscanf(input,"%lld",&t);
	fscanf(input,"%lld %lld",&a,&b);
	lld ar[a],as[9];
	fprintf(output,"Case #%lld:\n",t);
	lld count=0;
	for(i=32769;i<=65535;i+=2)
	{
//		cout<<"2";
		lld l,k;
		lld ans2,ans3,ans4,ans5,ans6,ans7,ans8,ans9,ans10;
		memset(ar,0,sizeof(ar));
		base2=decimal_binary(i);
//		cout<<i;
		tmp=base2;
		cout<<base2<<endl;
		for(j=0;j<a;j++)
		{
			tmp2=tmp%10;
			ar[j]=tmp2;
			tmp/=10;
		}
		as[0]=ans2=baseans(ar,2,a);
		as[1]=ans3=baseans(ar,3,a);
		as[2]=ans4=baseans(ar,4,a);
		as[3]=ans5=baseans(ar,5,a);
		as[4]=ans6=baseans(ar,6,a);
		as[5]=ans7=baseans(ar,7,a);
		as[6]=ans8=baseans(ar,8,a);
		as[7]=ans9=baseans(ar,9,a);
		as[8]=ans10=baseans(ar,10,a);
//		cout<<"s";
//		if(isprime(ans2)==0&&isprime(ans3)==0&&isprime(ans4)==0&&isprime(ans5)==0&&isprime(ans6)==0&&isprime(ans7)==0&&isprime(ans8)==0&&isprime(ans9)==0&&isprime(ans10)==0)
		
		if(isprime(ans2)==0){
//		cout<<"3";
		cout<<ans2<<" "<<ans3<<" "<<ans4<<" "<<ans5<<" "<<ans6<<" "<<ans7<<" "<<ans8<<" "<<ans9<<" "<<ans10<<endl;
//		cout<<ans2<<endl;
		for(k=0;k<9;k++)
		{
			for(l=2;l<as[k]/2;l++)
			{
				if(as[k]%l==0)
				{
					as[k]=l;
//					cout<<"1";
					break;
				}
			}
//			cout<<endl;
		}
//		cout<<"1";
		count++;
		fprintf(output,"%lld %lld %lld %lld %lld %lld %lld %lld %lld %lld\n",base2,as[0],as[1],as[2],as[3],as[4],as[5],as[6],as[7],as[8]);
	}
	else
		continue;
	if(count==b)
			break;
//		cout<<base2;
//		break;
	}
	return 0;
}
