#include<iostream>
using namespace std;
int main()
{
    int t, n, m, cnt, num;
    int arr1[4][4];
    int arr2[4][4];
    freopen("A-small-attempt2.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
	cin >> t;
	for(int i = 0; i < t ; i++)
	{
        cnt = 0;
        cin >> n;
        n--;
        for(int j = 0 ; j < 4 ; j++)
        {
             for(int k = 0 ; k < 4 ; k++)
             {
                  cin >> arr1[j][k];
             }
        }
        cin >> m;
        m--;
        for(int j = 0 ; j < 4 ; j++)
        {
             for(int k = 0 ; k < 4 ; k++)
             {
                  cin >> arr2[j][k];
             }
        }
        for(int j = 0 ; j < 4 ; j++)
        {
             for(int k = 0 ; k < 4 ; k++)
             {
                  if(arr1[n][j] == arr2[m][k])
                  {
                          cnt++;
                          num = arr1[n][j];
                  }
             }
        }
        if(cnt == 1)
             cout << "Case #" << i+1 << ": " << num;
        else if(cnt > 1)
             cout << "Case #" << i+1 << ": " << "Bad magician!";
        else if(cnt == 0)
             cout << "Case #" << i+1 << ": " << "Volunteer cheated!";
        if(i != t-1)
             cout << endl;
    }
    return 0;
}
