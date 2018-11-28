#include<iostream.h>
#include<fstream.h>
#include<conio.h>
#include<math.h>
int square(int n)
{
    int h = n & 0xF; // last hexidecimal "digit"
    if (h > 9)
        return 0; // return immediately in 6 cases out of 16.

    // Take advantage of Boolean short-circuit evaluation
    if ( h != 2 && h != 3 && h != 5 && h != 6 && h != 7 && h != 8 )
    {
        // take square root if you must
        int t = (int) floor( sqrt((double) n) + 0.5 );
            return t*t == n;
    }
    return 0;
}
int palindrome(int n)
{
    int dat[2000],size=0,i;
    while(n)
    {
            dat[size++]=n%10;
            n/=10;
    }
    for(i=0;i<size/2;i++)
                         if(dat[i]!=dat[size-i-1])
                              return 0;
    return 1;
}
int main()
{
    int t,i,j,k,a,b,cnt;
    ifstream fin("a.in");
    ofstream fout("a.out");
    fin>>t;
    //cout<<palindrome(121)<<palindrome(12)<<palindrome(121121);
    for(k=0;k<t;k++)
    {
                    fin>>a>>b;
                    cnt=0;
                    for(i=a;i<=b;i++)
                    {
                                     if(!square(i))
                                       continue;
                                     if(!palindrome(sqrt(i)))
                                       continue;
                                     if(!palindrome(i))
                                       continue;
                                     //cout<<"w="<<i<<endl;
                                     cnt++;
                    }
                    cout<<"Case #"<<k+1<<": "<<cnt<<endl;
                    fout<<"Case #"<<k+1<<": "<<cnt<<endl;
    }
    getch();
    
}
