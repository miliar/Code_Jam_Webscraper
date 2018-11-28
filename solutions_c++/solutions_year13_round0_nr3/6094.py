#include<fstream.h>
#include<math.h>
using namespace std;
fstream fout("Sample.out");
fstream fin("Sample.in");
int palindrome(int n)
{
    int a = 0;
    for(int tn = n; tn > 0; tn /= 10)
        a = (a * 10) + (tn % 10);
    if(a == n)
        return 1;
    else
        return 0;
}
int square(int n)
{
    float root = sqrt(n);
    int Root = root;
    if(root == (float)Root)
        return Root;
    else
        return 0;
}
int main()
{
    int cases,a,b;
    fin >> cases;
    for(int C = 1; C <= cases; C++)
    {
        int count = 0;
        fin >> a >> b;
        for(int i = a; i <= b; i++)
        {
            int ctr = palindrome(i);
            if(ctr)
            {
                int CTR = square(i);
                if(CTR)
                {
                    int final = palindrome(CTR);
                    if(final)
                        count++;
                }
            }
        }
        fout << "Case #" << C << ": " << count << '\n';
    }
}       
