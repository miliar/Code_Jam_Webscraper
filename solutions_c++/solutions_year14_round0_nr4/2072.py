
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iostream>

using namespace std;
int n;
double x[1000],y[1000],p[1000],q[1000];


int partition(double arr[],int low,int high,int pivot_index){
	int store_index = low;
	double pivot_value = arr[pivot_index];
	double tmp;
	//move pivot to the end
	tmp = arr[pivot_index];
	arr[pivot_index] = arr[high];
	arr[high] = tmp;

//	swap(arr[pivot_index],arr[high]);
	for (int i=low; i < high ; ++i)
	{
		if(arr[i] <= pivot_value){
			tmp = arr[i];
			arr[i] = arr[store_index];
			arr[store_index] = tmp;
//			swap(arr[i],arr[store_index]);
			store_index++;
		}
	}
	tmp = arr[store_index];
	arr[store_index] = arr[high];
	arr[high] = tmp;
//	swap(arr[store_index],arr[high]);
	return store_index;
}
void quiksort(double arr[],int low,int high){
	if(low < high ){
		int piv_index = low +(high-low)/2;
		int new_index = partition(arr,low,high,piv_index);
		quiksort(arr,low,new_index-1);
		quiksort(arr,new_index+1,high);
	}
}

int war()
{
    int win=0;
    for(int i=0;i<n;i++)
      for(int j=i;j<n;j++)
        if(x[i]<y[j])
            {
                win++;
                y[j]=0;
                break;
            }

    return n-win;
}

int Dwar()
{

  /*  for(int i=0;i<n;i++)
                printf("%0.7lf ", p[i]);
    printf("\n");
    for(int i=0;i<n;i++)
                printf("%0.7lf ", q[i]);
*/
    int win=0,k=n-1;
    for(int i=0;i<n;i++)
    {int flag=0;
        for(int j=0;j<n;j++)
        {
            if(p[i]>q[j] && q[j]!=0)
            {   //printf("%lf",p[i]);
                win++;
                q[j]=0;
                flag=1;
                break;
            }
        }
        if(flag==0)
            q[k--]=0;
    }

    return win;
}

int main() {
    freopen("A-smallx.in", "r", stdin);
    freopen("small.txt", "w", stdout);
    int T;
    int ans1,ans2;

    scanf("%d", &T);
    for(int t = 1; t <= T; ++t) {
        scanf("%d", &n);

        for(int i=0;i<n;i++)
            {scanf("%lf", &x[i]);
            }
        for(int i=0;i<n;i++)
            {scanf("%lf", &y[i]);
            }
        quiksort (x, 0, n-1);
        quiksort (y, 0, n-1);
        for(int i=0;i<n;i++)
            {
                p[i]=x[i];
                q[i]=y[i];
            }

        ans1=war();
        ans2=Dwar();

        printf("Case #%d: %d %d\n", t, ans2 ,ans1);
    }

	return 0;
}

