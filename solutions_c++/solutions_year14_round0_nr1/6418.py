#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<climits>
#include<cstring>
#include<algorithm>
#include<stack>
#include<vector>
#include <fstream>

using namespace std;

void magician(int arr1[4][4], int ans1, int arr2[4][4], int ans2, int count)
{
	int *row1 = new int[4];
	for(int i=0; i<4; i++)
		row1[i] = arr1[ans1-1][i];

    int *row2 = new int[4];
    for(int i=0; i<4; i++)
        row2[i] = arr2[ans2-1][i];

    int sameFlag = 0,  res = -1;

    for(int i=0; i<4; i++)
    {
        if(row1[i] == row2[0] || row1[i] == row2[1] || row1[i] == row2[2] || row1[i] == row2[3])
        {
            sameFlag = sameFlag + 1;
            res = row1[i];
        }
    }

   FILE *f = fopen("output.txt", "a");

    if(sameFlag  == 1)
        fprintf(f, "Case #%d: %d\n", count, res);
    else if(sameFlag > 1)
        fprintf(f, "Case #%d: Bad magician!\n", count);
    else if(sameFlag == 0)
        fprintf(f, "Case #%d: Volunteer cheated!\n", count);

     fclose(f);
}

int main()
{
	int arr1[4][4];
	int arr2[4][4];

	int ans1, ans2;

	int num, count = 1;

    ifstream infile("A-small-attempt1.in");
    infile >> num;

	while(num--)
	{
		infile >> ans1;

		for(int i=0; i<4; i++)
			infile >> arr1[i][0] >> arr1[i][1] >> arr1[i][2] >> arr1[i][3];

		infile >> ans2;

		for(int i=0; i<4; i++)
			infile >> arr2[i][0] >> arr2[i][1] >> arr2[i][2] >> arr2[i][3];

		magician(arr1, ans1, arr2, ans2, count);
		count = count + 1;
	}
}


