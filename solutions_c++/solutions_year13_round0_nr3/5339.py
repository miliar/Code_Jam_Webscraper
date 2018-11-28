#include<cstdio>
#include<iostream>

using namespace std;

int main()

{
        int t,i;
        int a[] = {1,4,9,121,484};
        
        int T,A,B;
        cin >> T;
        t = T;
        while(T--)
        {
                cin >> A >> B;
                int count = 0;
                for(i = 0 ; i < 5; i++)
                {
                        if(a[i] <= B && a[i] >= A)
                                count ++;
                }
                cout << "Case #" <<t-T <<": " << count << endl;
        }
        
        
}