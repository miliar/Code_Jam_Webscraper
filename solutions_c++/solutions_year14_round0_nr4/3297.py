#include <iostream>
#include <algorithm>
#include <fstream>

using namespace std;

bool cmp(double *p, double* q)
{
    return p[0] < q[0];
}

int main()
{
    int cases = 0;
    int count = 1;
    cin >> cases;
    while(count <= cases)
    {
        int n;
        cin >> n;
        double** naomi = new double*[n];
        double** ken = new double*[n];

        for(int i = 0; i < n; i++)
        {
            naomi[i] = new double[2];
            cin >> naomi[i][0];
            naomi[i][1] = 0.0;
        }

        for(int i = 0; i < n; i++)
        {
            ken[i] = new double[2];
            cin >> ken[i][0];
            ken[i][1] = 0.0;
        }

        sort(ken, ken + n, cmp);
        sort(naomi, naomi + n, cmp);
/*        for(int i = 0; i < n; i++)
        {
            cout << naomi[i][0] << ' ';
        }
        cout << endl;

        for(int i = 0; i < n; i++)
        {
            cout << ken[i][0] << ' ';
        }
        cout << endl;
*/
        int normal = 0;
        int deceitful = 0;

        for( int i = n - 1; i >= 0; i--)
        {
            //cout << naomi[i][0] << ' ';
            double nao = naomi[i][0];
            int m_index = -1;
            int flag = 0;
            for(int j = 0; j < n; j++)
            {
                if(ken[j][1] < 1.0 && m_index < 0)
                {
                    m_index = j;
                }

                if(ken[j][0] > nao && ken[j][1] < 1.0)
                {
                    flag = 1;
                    ken[j][1] = 1.5;
                   //cout << ken[j][0] << endl;
                    break;
                }
            }

            if(flag == 0)
            {
                ken[m_index][1] = 1.5;
                normal++;
                //cout << ken[m_index][0] << endl;
            }
        }

	for(int i = 0; i < n; i++)
	{
		double k = ken[i][0];
		for(int j = 0; j < n; j++)
		{
			if(naomi[j][0] > k && naomi[j][1] < 1.0)
			{
				deceitful++;
				naomi[j][1] = 1.5;
				break;
			}
		}

	}


        cout << "Case #" << count << ": " << deceitful << " " << normal << endl;
        count++;
    }
    return 0;
}
