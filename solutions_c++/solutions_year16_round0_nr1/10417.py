#include <iostream>
#include <set>
#include <list>

#include <stdio.h>

using namespace std;



int T,N,digit,temp;
int main()
{
    //scanf("%d",&T);
    cin>>T;
	for(int i = 1 ; i <= T ; i++)
    {
        //scanf("%d",&N);
        cin>>N;
		if(N==0)
        {
            printf("Case #%d: %s\n",i,"INSOMNIA");
                continue;
        }
        set<int> digits;
        for(int j = N, k = 1 ; (int)digits.size() < 10;k++)
        {
            j = N * k;
            temp = j;
            while (temp)
            {

            digits.insert(temp%10);

            if((int)digits.size() == 10 )
            {
                printf("Case #%d: %d\n",i,j);
                break;
            }
            temp /= 10;
            }


        }


    }


    return 0;
}
