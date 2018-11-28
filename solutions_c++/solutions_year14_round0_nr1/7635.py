#include<stdio.h>
#include<vector>
#include<algorithm>
#define RowSize 4
using namespace std;

void scanAndReadVector(vector<int> *v)
{
    int vLoc,temp;

    /* get the row location */
    scanf("%d",&vLoc);

    /* skip the rows before location */
    for(int i = 1;i <= (vLoc-1)*RowSize; i++)
    scanf("%d",&temp);

    /* read the desire row */
    for(int i = 1;i <= RowSize; i++)
    {
        scanf("%d",&temp);
        (*v).push_back(temp);
    }

    /* skip the rows after location */
    for(int i = 1;i <= (4-vLoc)*RowSize; i++)
    scanf("%d",&temp);

}

void ProcessMagic(int testCaseNumber)
{
    vector<int> v1,v2,vCommon;

    v1.reserve(RowSize);
    v2.reserve(RowSize);
    vCommon.reserve(RowSize);

    scanAndReadVector(&v1);
    scanAndReadVector(&v2);

    sort(v1.begin(), v1.end());
    sort(v2.begin(), v2.end());

    set_intersection(v1.begin(), v1.end(),
                     v2.begin(), v2.end(),
                     back_inserter(vCommon));

    int vCommonSize = vCommon.size();

    printf("Case #%d: ",testCaseNumber);

    if(vCommonSize == 1)
        printf("%d\n",vCommon[0]);
    else if (vCommonSize == 0)
        printf("Volunteer cheated!\n");
    else if (vCommonSize > 1)
        printf("Bad magician!\n");

}

int main()
{
    freopen("MagicTrick_ip.txt","r",stdin);
    freopen("MagicTrick_op.txt","w",stdout);

    int numberOfTestCases = 0;
    scanf("%d",&numberOfTestCases);

    for(int testCaseNumber=1; testCaseNumber<=numberOfTestCases; testCaseNumber++)
    ProcessMagic(testCaseNumber);

    return 0;
}
