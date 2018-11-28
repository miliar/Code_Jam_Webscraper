

#include <iostream>
using namespace std;
bool judge(int** lawn, int a, int b);
int main()
{
	int T;
	cin>>T;
	int q=1;
	while(q<=T)
	{
		int a,b;
		cin >>a;
		cin >>b;
		int **lawn = new  int* [a];

		for(int i =0;i<a;i++){
			lawn[i] = new int[b];
			for(int j=0;j<b;j++){
				cin>>lawn[i][j];
			}
		}
		if(judge(lawn,a,b))
			cout<<"Case #"<<q<<": "<<"YES"<<endl;
		else
			cout<<"Case #"<<q<<": "<<"NO"<<endl;

		delete [] lawn;
		q++;
	}
	return 0;
}

bool judge(int** lawn, int a, int b){
	for(int i =0;i<a;i++)
	{
		for(int j=0;j<b;j++)
		{
			bool f1 = true, f2 = true; 
			int c = lawn[i][j];
		
			for(int m =0;m<a;m++){
				if(lawn[m][j]>c){
					f1 =false;
					break;
				}
			}

			for(int m=0;m<b;m++)
			{
				if(lawn[i][m]>c)
				{
					f2 =false;
					break;
				}
			}
			if(f1==false&&f2==false)
				return false;
		}
	}
	return true;
}