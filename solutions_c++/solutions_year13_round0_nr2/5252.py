#include<iostream>
#include<string>
#include<sstream>
#include<cstdio>
#include<cstring>


using namespace std;

int a[100][100];
int b[200];



int greatest1(int a[], int size);


int main()
{




	freopen("B-large.in","r",stdin);
	freopen("result.out","w",stdout);

	int N,count=0;
	cin>>N;
	cin.ignore();


	while(N--){
	
		memset(b,0,sizeof(b[0])*200);

		count++;
		int n,m;
		string s;
		getline(cin,s);
		istringstream is(s);

		is>>n;
		is>>m;

		

		for(int i=0;i<n;i++){
			string temp;
			getline(cin,temp);

			istringstream is1(temp);

			for(int j=0;j<m;j++)
				is1>>a[i][j];

		}

		/*Test print matrix
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				cout<<a[i][j]<<" ";
			}
			cout<<endl;
		}
		*/

		//Store maximum elements in rows
		for(int i=0;i<n;i++){
			b[i] = greatest1(a[i],m);
		}

		//store maximum element for columns
		int temp[n];

		for(int i=0;i<m;i++){
			for(int j=0;j<n;j++){
				temp[j] = a[j][i];
			}

			b[i+100] = greatest1(temp,n);

		}


		/*test
		for(int i=0;i<20;i++)
			cout<<b[i]<<" ";
		cout<<endl;
		*/

		int check = 0;

		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){

				if(b[i]!=a[i][j] && b[j+100]!=a[i][j]){
					check =1;
					//cout<<"TEST "<<a[i][j]<<endl;
				}
			}
		}

		if(check == 1)
			printf("Case #%d: NO\n",count);
		else
			printf("Case #%d: YES\n",count);

	}

	return 0;
}


int greatest1(int a[], int size)
{
	int max;
	max = a[0];
	for(int i=1;i<size;i++)
		if(a[i]>max)
			max = a[i];
	return max;
}


