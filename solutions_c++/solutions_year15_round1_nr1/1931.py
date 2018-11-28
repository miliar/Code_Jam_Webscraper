#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;
int main()
{
	fstream file1,file2;
	file1.open("A.in",ios::in);
	file2.open("b.txt",ios::out);
	int a,n[1010],num,ans1,ans2,k=0,dif[1010],big;
	file1>>a; //scanf("%d",&a);
	while(a--)
	{
		k++;
		ans1=ans2=big=0;
		file1>>num; //scanf("%d",&num);
		for(int q=0;q<num;++q)
			file1>>n[q]; //scanf("%d",&n[q]);
		for(int q=0;q<num-1;++q)
			dif[q]=n[q]-n[q+1];
		for(int q=0;q<num-1;++q)
		{
			if(dif[q]>0)
				ans1+=dif[q];
			big=max(big,dif[q]);
		}
		for(int q=0;q<num-1;++q)
			ans2+=min(big,n[q]);
		file2<<"Case #"<<k<<": "<<ans1<<" "<<ans2<<"\n"; //printf("Case #%d: %d %d\n",k,ans1,ans2);
	}
 	return 0;
}

