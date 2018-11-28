#include <bits/stdc++.h>

using namespace std;

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

  int tt;
  scanf("%d", &tt);
  for (int qq = 1; qq <= tt; qq++) {

    //---------------------------------------------------------------------------------------------
    // input data starts
    //---------------------------------------------------------------------------------------------
    string seq, ss;
    int l, i;
    cin>>seq;
    l=seq.length();
    for (i=0;i<l;++i)
    {
        ss = seq[i];
        if (seq[i]>=seq[0])
        {
            seq.insert(0,ss);
            seq.erase(i+1,1);
        }
    }



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

    cout<<seq<<endl;

    //---------------------------------------------------------------------------------------------
    // solution ends
    //---------------------------------------------------------------------------------------------

    fflush(stdout);
    fprintf(stderr, "test %d solved, time = %d ms\n", qq, (int)clock());
  }
  return 0;
}
