#include <iostream>
#include <vector>

using namespace std;

void sort(double *array, int n)
{
    for(int x=0; x<n; x++)
    {
        for(int y=0; y<n-1; y++)
        {
			if(array[y]>array[y+1])
			{
				double temp = array[y+1];
				array[y+1] = array[y];
				array[y] = temp;
			}
		}
	}
}

int main()
{
    int t;
    cin >> t;

    int *scoreDecWar = new int[t], *scoreWar = new int[t];

    for (int i = 0; i < t; i++)
    {
        int n;
        cin >> n;

        double *b1 = new double[n];
        double *b2 = new double[n];

        for (int j = 0; j < n; j++)
            cin >> b1[j];
        for (int j = 0; j < n; j++)
            cin >> b2[j];

        scoreDecWar[i] = 0;
        scoreWar[i] = 0;

        sort(b1, n);
        sort(b2, n);

        vector<double> v1, v2;

        for (int j = n - 1; j >= 0; j--)
        {
            v1.push_back(b1[j]);
            v2.push_back(b2[j]);
        }
        for (int j = n - 1; j >= 0; j--)
        {
            b1[j] = v1[j];
            b2[j] = v2[j];
        }

        while (v1.size() != 0)
        {
            if (v1[0] > v2[0])
            {
                v1.erase(v1.begin());
                v2.erase(v2.begin());

                scoreDecWar[i]++;
            }
            else
            {
                v1.pop_back();
                v2.erase(v2.begin());
            }
        }

        int temp = n-1;
        for (int j = n-1; j >= 0; j--)
        {
            while (b2[temp] < b1[j])
            {
                scoreWar[i]++;
                temp--;

                if (temp < 0)
                    break;
            }
            temp--;
            if (temp < 0)
                break;
        }

        delete[] b1;
        delete[] b2;
    }

    for (int i = 0; i < t; i++)
        cout << "Case #" << (i+1) << ": " << scoreDecWar[i] << " " << scoreWar[i] << endl;

    delete[] scoreDecWar;
    delete[] scoreWar;

    return 0;
}
