 
#include<iostream>
#include<fstream>
using namespace std;


bool checkElement(int arr[101][101], int i, int j, int n, int m) 
	{
        int num = arr[i][j];
        bool isOk = true;
       
        for (int k = 0; k < m; k++)
		 {
            if (num < arr[i][k]) {
                isOk = false;
                break;
            }
        }
        if (isOk)
            return true;
        isOk = true;
        // check vertical
        for (int k = 0; k < n; k++) {
            if (num < arr[k][j]) {
                isOk = false;
                break;
            }
        }
        return isOk;
    }


     bool check (int arr[101][101], int n, int m)
	  {
        for (int i = 0; i < n; i++) 
		{
            for (int j = 0; j < m; j++) 
			{
                if (!checkElement(arr, i, j, n, m))
                    return false;
            }
        }
        return true;
    }

    


		int main()
		{
			
			freopen("B.in","r",stdin);
			freopen("B-large.out","w",stdout);
			int t,n,m;
			cin>>t;
			int p=0;
			while(t--)
			{
				int arr[101][101];
				cin>>n>>m;
						
            	for (int i = 0; i < n; i++)
                for (int j = 0; j < m; j++)
                    cin>>arr[i][j];
                    
            cout<<"Case #" <<p+1<<": "<< (check(arr, n, m) ? "YES" : "NO")<<endl;
            
            p++;
        }
    }
