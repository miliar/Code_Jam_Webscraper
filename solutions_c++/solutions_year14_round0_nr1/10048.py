#include<iostream>
#include<stdlib.h>
int s;
int compare(int *a,int b)
{
    int j,x=0;
    for(j=0;j<4;j++)
    {
        if(a[j]==b)
        {
            x++;
            s = b;
        }
    }
    return x;

}

int main()
{
    int T,q;
    std::cin >> T;
    for(q=0;q<T;q++)
    {
        int r1,r2,c=0;
        int *A1 = (int *) malloc(4*sizeof(int));
        int *A2 = (int *) malloc(4*sizeof(int));
        std::cin >> r1;
        int i,j,t;
        for(j=0;j<4;j++)
        {
            for(i=0;i<4;i++)
            {
                std::cin >> t;
                if(j==r1-1)
                A1[i] = t;
            }
        }
        std::cin >> r2;
        for(j=0;j<4;j++)
        {
            for(i=0;i<4;i++)
            {
                std::cin >> t;
                if(j==r2-1)
                {
                    A2[i] = t;
                    c += compare(A1,A2[i]);
                    //std::cout << c << "\n";
                }
            }
        }
        std::cout << "case #" << q+1;
        if(c==0)
        std::cout << ": Volunteer cheated!\n";
        else if(c==1)
        std::cout << ": " << s << "\n";
        else
        std::cout << ": Bad magician!\n";
    }
    return 0;
}
