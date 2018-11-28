
#include <map>

#include <cstdlib>
#include <cstdio>

static const int maxLen = 1024;

#if 0
#define dprintf printf
#else
#define dprintf //
#endif

static bool solve( FILE *fd, char *inputBuf )
{
    int numChars = getline( &inputBuf,
                            (size_t*)&maxLen,
                            fd );

    int row;
    int col;
    sscanf( inputBuf, "%d %d", &row, &col );
    dprintf("size: %d x %d\n", row, col);

    int lawn[row][col];

    for( int i=0; i<row; ++i )
    {
        int numChars = getline( &inputBuf,
                                (size_t*)&maxLen,
                                fd );

        char *tok = strtok( inputBuf, " " );

        for( int k=0; k<col; ++k )
        {
            if( tok == NULL )
            {
                break;
            }

            lawn[i][k] = atoi( tok );
            dprintf("%d ", lawn[i][k]);

            tok = strtok( NULL, " " );
        }
        dprintf("\n");
    }

    // can always mow a width of 1
    if( (row == 1) || (col == 1) )
    {
        return true;
    }

    // Mow!
    for( int i=0; i<row; ++i )
    {
        for( int k=0; k<col; ++k )
        {
            int h = lawn[i][k];

            bool mowable_row = true;
            bool mowable_col = true;

            for( int t=0; t<row; ++t )
            {
                if( lawn[t][k] > h )
                {
                    mowable_col = false;
                    break;
                }
            }
        
            for( int t=0; t<col; ++t )
            {
                if( lawn[i][t] > h )
                {
                    mowable_row = false;
                    break;
                }
            }

            if( !mowable_col && !mowable_row )
            {
                return false;
            }
        }
    }

    return true;
}



int main( int argc, char **argv )
{
    if( argc < 2 )
    {
        printf("!!! NO INPUT FILE !!!\n");
        return -1;
    }

    FILE *fd = (FILE*)fopen(argv[1], "r");

    char *inputBuf = (char*)malloc(maxLen);
    getline( &inputBuf,
             (size_t*)&maxLen,
             fd );

    int cases = strtol(inputBuf, NULL, 10);
    free(inputBuf);

    inputBuf = (char*)malloc(maxLen);

    for( int caseNum=0; caseNum < cases; caseNum++ )
    {
        bool answer = solve( fd, inputBuf );

        printf("Case #%d: %s\n", caseNum+1, (answer) ? "YES" : "NO" );
    }

    free(inputBuf);
    fclose(fd);

    return 0;
}

