#include <iostream>
using namespace std;

int arr[10][10];
int row[10],col[10];

//bool checkRow(int n,int m,int index);
//bool checkCol(int n,int m,int index);

int main(){
	int T,N,M,j=0;
	freopen("B-small-attempt2.in","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>T;
	for(int i = 1; i <= T ; i++)
	{
		memset(row,0,sizeof(row));
		memset(col,0,sizeof(col));

		cin>>N>>M;

		j = N;

		for(int k=0;k<N;k++)
		{
			for(int h = 0;h<M;h++)
			{
				cin>>arr[k][h];
				if(arr[k][h] > row[k])
					row[k] = arr[k][h];
				if(arr[k][h] > col[h])
					col[h] = arr[k][h];
			}
		}

		for(int k=0;k<N;k++)
		{
			for(int h=0;h<M;h++)
			{
				if(arr[k][h] == row[k] || arr[k][h] == col[h])
				{
					j = N;
					continue;
				}
				else
				{
					j = N-1;
					break;
				}
			}
			if(j != N)
				break;
		}

		/*for(j = 0;j<N;j++)
		{
			if(!checkRow(N,M,j))
				break;
		}*/

		cout<<"Case #"<<i<<": ";
		if(j==N)
			cout<<"YES";
		else
			cout<<"NO";
		cout<<endl;
	}
	return 0;
}
//
//bool checkRow(int n, int m, int index)
//{
//	if(row[index]) return true;
//	int ref = arr[index][0];
//	for(int i=1;i<m;i++)
//	{
//		if(arr[index][i] >= ref)
//		{
//			continue;
//		}
//		else if(arr[index][i] < ref)
//		{
//			int z = index;
//			/*if(z == 0 || z == n-1 || i == 0 || i = m-1)
//			{*/
//				if(checkCol(n,m,i))
//				{
//					continue;
//				}
//				else
//				{
//					return false;
//				}
//			/*}
//			else
//			{
//				return false;
//			}*/
//		}
//	}
//	row[index] = true;
//	return true;
//}
//
//bool checkCol(int n, int m, int index)
//{
//	if(col[index]) return true;
//	int ref = arr[0][index];
//	for(int i=1;i<n;i++)
//	{
//		if(arr[i][index] == ref)
//		{
//			continue;
//		}
//		else
//		{
//			/*if(checkRow(n,m,i))
//			{
//				continue;
//			}
//			else
//			{*/
//				return false;
//			//}
//		}
//	}
//	col[index] = true;
//	return true;
//}


//#include<iostream>
//using namespace std;
//
//int main()
//{
//	freopen("C-small-attempt1.in","r",stdin);
//	freopen("output.txt","w",stdout);
//
//	int t,n,a,b,arr[] = {1,4,9,121,484};
//	cin>>t;
//	for(int i=1;i<=t;i++)
//	{
//		n=0;
//		cin>>a>>b;
//		if(arr[0] >=a && arr[0]<=b)
//			n++;
//		if(arr[1] >=a && arr[1]<=b)
//			n++;
//		if(arr[2] >=a && arr[2] <=b)
//			n++;
//		if(arr[3] >=a && arr[3] <=b)
//			n++;
//		if(arr[4] >=a && arr[4] <=b)
//			n++;
//		cout<<"Case #"<<i<<": "<<n<<endl;
//	}
//
//	return 0;
//}