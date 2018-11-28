#include <iostream>
using namespace std;
int sum,ii;


int main() {
    int a,b,c,n;
    int sum;
    int arr[60];
    cin>>n;
    for (int i=0;i<n; i++)
    {
        cin>>a>>b>>c;
        sum=0;
        for (int aa=0; aa<a; aa++)
            for (int bb=0; bb<b; bb++)
                if ( (aa & bb) < c)
                {
                    sum++;
                }
        cout<<sum<<endl;
    }
	return 0;
}