#include <bits/stdc++.h>

using namespace std;
int sumarr(int a[])
{
    int sum=0;
    for (int j=0; j<10; j++)
    {
        sum+=a[j];
    }

    return sum;
}
int main(int argc, char* argv[]) {
  int TEST_FROM = 0;
  int TEST_TO = 123456789;
  if (argc == 3) {
    sscanf(argv[1], "%d", &TEST_FROM);
    sscanf(argv[2], "%d", &TEST_TO);
  }
  //freopen("small.in", "r", stdin);
  //freopen("small.out", "w", stdout);
  freopen("large.in", "r", stdin);
  freopen("large.out", "w", stdout);

  int tt, i, a, m[10]={0};
  long long n, x, ans;
  scanf("%d", &tt);
  for (int qq = 1; qq <= tt; qq++) {

    //---------------------------------------------------------------------------------------------
    // input data starts
    //---------------------------------------------------------------------------------------------

    cin>>n;

    //---------------------------------------------------------------------------------------------
    // input data ends
    //---------------------------------------------------------------------------------------------
                    if (qq < TEST_FROM || qq > TEST_TO) {
                        continue;
                    }
                    printf("Case #%d: ", qq);
                    fflush(stdout);
    //---------------------------------------------------------------------------------------------
    // solution starts
    //---------------------------------------------------------------------------------------------


    for (int k=0; k<10; k++)
    {
        m[k]=0;
    }

    for (i=1; i<=100*n; i++)
    {

        x=n*i;

        while (x>0)
        {
            a=x%10;
            x=x/10;
            m[a]=1;

        }
        if (sumarr(m)==10) break;
    }


    ans=n*i;
    if (sumarr(m)==10)
    {
        printf("%d\n", ans);
    }
    else
    {
        cout<<"INSOMNIA"<<endl;
    }




    //---------------------------------------------------------------------------------------------
    // solution ends
    //---------------------------------------------------------------------------------------------

    fflush(stdout);
    fprintf(stderr, "test %d solved, time = %d ms\n", qq, (int)clock());
  }
  return 0;
}
