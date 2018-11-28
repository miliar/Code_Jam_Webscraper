#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
	ios_base::sync_with_stdio(false);

    int T;  cin >> T;

    for (int i = 0; i < T; i++)
    {
        int D;  cin >> D;
        int pan[1001] = {0};
		int pan1[1001] = {0};
        int max, Spl = 0, Div, NDiv;

        for (int j = 0,n; j < D; j++)
        {
            cin >> n;
            pan[n]++;	pan1[n]++;
        }
        for (int j = 1000; j > 0; j--)
            if(pan[j])
            {
                max = j;
                break;
            }

			int max1 = max;
		do
        {
            NDiv = max1 + Spl;
            if (max1 % 2 == 0)
            {
                Div = Spl + pan1[max1] + pan1[max1-1];
                pan1[max1/2] += 2 * pan1[max1] + pan1[max1-1];
                pan1[(max1/2)-1] += pan1[max1-1];
                for ( int j = max1 - 2; j > 0; j--)
                    if(pan1[j])
                    {
                        max1 = j;    break;
                    }
            }
            else
            {
                Div = Spl + pan1[max1];
				if (max1 == 9)
				{

					pan1[3] += pan1[max1];
					pan1[6] += pan1[max1];
				}
				else
				{
					pan1[max1/2] += pan1[max1];
                pan1[(max1/2)+1] += pan1[max1];
				}
                for ( int j = max1 - 1; j > 0; j--)
                    if(pan1[j])
                    {
                        max1 = j;    break;
                    }
            }
            Spl = Div;
            Div += max1;
        }while(NDiv >= Div);
		int N1 = NDiv;
		Spl = 0;
		 do
        {
            NDiv = max + Spl;
            if (max % 2 == 0)
            {
                Div = Spl + pan[max] + pan[max-1];
                pan[max/2] += 2 * pan[max] + pan[max-1];
                pan[(max/2)-1] += pan[max-1];
                for ( int j = max - 2; j > 0; j--)
                    if(pan[j])
                    {
                        max = j;    break;
                    }
            }
            else
            {
                Div = Spl + pan[max];
                pan[max/2] += pan[max];
                pan[(max/2)+1] += pan[max];
                for ( int j = max - 1; j > 0; j--)
                    if(pan[j])
                    {
                        max = j;    break;
                    }
            }
            Spl = Div;
            Div += max;
        }while(NDiv >= Div);
		int N2 = NDiv;

		if (N1 < N2) NDiv = N1;
		else	NDiv = N2;
        cout << "Case #" << i+1 << ": " << NDiv << '\n';
    }
    return 0;
}
