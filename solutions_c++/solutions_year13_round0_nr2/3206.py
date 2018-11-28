#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

class stMatrix {
public:
    stMatrix(int rows, int cols);
    ~stMatrix();

    void addRow(int row, int *vals);
    int maxRow(int row) const;
    int maxCol(int col) const;

    bool isPossible() const;

private:
    int m_rows;
    int m_cols;
    int **m_vals;
    int **m_chks;

    stMatrix();
};

stMatrix::stMatrix(int rows, int cols)
    : m_rows(rows), 
      m_cols(cols)
{
    m_vals = (int **)calloc(rows, sizeof(int *));
    m_chks = (int **)calloc(rows, sizeof(int *));
    for (int r = 0; r < rows; r++)
    {
        m_vals[r] = (int *)calloc(cols, sizeof(int));
        m_chks[r] = (int *)calloc(cols, sizeof(int));
    }
}

stMatrix::~stMatrix()
{
    for (int r = 0; r < m_rows; r++)
    {
        free(m_vals[r]);
        free(m_chks[r]);
    }
    free(m_vals);
    free(m_chks);
}

void
stMatrix::addRow(int row, int *vals)
{
    for (int c = 0; c < m_cols; c++)
    {
        //printf("%d ", vals[c]);
        m_vals[row][c] = vals[c];
    }
    //printf("\n");
}

int
stMatrix::maxRow(int row) const
{
    int mx = 0;
    for (int c = 0; c < m_cols; c++)
    {
        if (m_vals[row][c] > mx)
            mx = m_vals[row][c];
    }
    return mx;
}

int
stMatrix::maxCol(int col) const
{
    int mx = 0;
    for (int r = 0; r < m_rows; r++)
    {
        if (m_vals[r][col] > mx)
            mx = m_vals[r][col];
    }
    return mx;
}


bool
stMatrix::isPossible() const
{
    for (int r = 0; r < m_rows; r++)
    {
        for (int c = 0; c < m_cols; c++)
        {
            int max_row = maxRow(r);
            int max_col = maxCol(c);
            int mn = (max_row < max_col ? max_row : max_col);
            if (mn > m_vals[r][c])
                return false;
        }
    }
    return true;
}

void
readRowCols(char *buf, int *rowCols)
{
    char *ptr = strchr(buf, ' ');
    *ptr = '\0';
    rowCols[0] = atoi(buf);
    rowCols[1] = atoi(ptr+1);
}

void
getHeightVals(char *buf, int *heightVals)
{
    char *ptr = buf;
    char *p2;
    int c = 0;
    while ((p2 = strchr(ptr, ' ')) != NULL)
    {
        *p2 = '\0';
        int val = atoi(ptr);
        heightVals[c] = val;
        c++;
        ptr = p2+1;
    }

    int val = atoi(ptr);
    heightVals[c] = val;
}

int
main(int argc, char **argv)
{
    if (argc != 2)
    {
        printf("Usage: %s <input.txt>\n", argv[0]);
        return 0;
    }

    FILE *f = fopen(argv[1], "r");
    if (!f)
    {
        printf("Couldn't open file\n");
        return 0;
    }

    char buf[10001];
    fgets(buf, 10001, f);
    int num_lawns = atoi(buf);
    //printf("There are %d lawns\n", num_lawns);

    int heightVals[1000];

    for (int lawn_num = 0; lawn_num < num_lawns; lawn_num++)
    {
        fgets(buf, 10001, f);
        int rowCols[2];
        readRowCols(buf, rowCols);
        int num_rows = rowCols[0];
        int num_cols = rowCols[1];
        //printf("Got %dx%d\n", num_rows, num_cols);
        stMatrix *lawn = new stMatrix(num_rows, num_cols);
        for (int row = 0; row < num_rows; row++)
        {
            fgets(buf, 10001, f);
            getHeightVals(buf, heightVals);
            lawn->addRow(row, heightVals);
        }
        printf("Case #%d: ", lawn_num+1);
        if (lawn->isPossible())
            printf("YES\n");
        else
            printf("NO\n");
        delete lawn;
    }

    fclose(f);

    return 0;
}
