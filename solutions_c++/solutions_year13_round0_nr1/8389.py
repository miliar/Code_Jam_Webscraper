#define null 0

#include <iostream>

const int CELL_WIDTH = 4;
const int CELL_HEIGHT = 4;

enum Result
{
    Result_WinO,
    Result_WinX,
    Result_Draw,
    Result_NotCompleted,
    Result_Num
};

enum CellType
{
    CellType_O,
    CellType_X,
    CellType_T,
    CellType_S,
    CellType_Num
};

struct Board
{
    CellType a[CELL_HEIGHT][CELL_WIDTH];
};

Result CheckBoard(const Board& board)
{
    bool isDraw = true;

    // check row
    for (int y = 0; y < CELL_HEIGHT; ++y)
    {
        bool fault = false;
        
        CellType startType = board.a[y][0];
        for (int x = 1; x < CELL_WIDTH; ++x)
        {
            if (board.a[y][x] == CellType_S)
            {
                isDraw = false;
            }
            
            if (startType != board.a[y][x] &&
                board.a[y][x] != CellType_T)
            {
                fault = true;
                break;
            }
        }

        if (!fault)
        {
            if (startType == CellType_O)
            {
                return Result_WinO;
            }
            else if (startType == CellType_X)
            {
                return Result_WinX;
            }
        }
    }

    // check colun
    for (int x = 0; x < CELL_WIDTH; ++x)
    {
        bool fault = false;
        
        CellType startType = board.a[0][x];
        for (int y = 1; y < CELL_HEIGHT; ++y)
        {
            if (startType != board.a[y][x] &&
                board.a[y][x] != CellType_T)
            {
                fault = true;
                break;
            }
        }

        if (!fault)
        {
            if (startType == CellType_O)
            {
                return Result_WinO;
            }
            else if (startType == CellType_X)
            {
                return Result_WinX;
            }
        }
    }

    // check cross
    {
        bool fault = false;
        CellType startType = board.a[0][0];
        for (int i = 1; i < CELL_HEIGHT; ++i)
        {
            if (startType != board.a[i][i] &&
                board.a[i][i] != CellType_T)
            {
                fault = true;
                break;
            }
        }

        if (!fault)
        {
            if (startType == CellType_O)
            {
                return Result_WinO;
            }
            else if (startType == CellType_X)
            {
                return Result_WinX;
            }
        }
    }
    {
        bool fault = false;
        CellType startType = board.a[0][3];
        for (int i = 1; i < CELL_HEIGHT; ++i)
        {
            if (startType != board.a[i][3 - i] &&
                board.a[i][3 - i] != CellType_T)
            {
                fault = true;
                break;
            }
        }

        if (!fault)
        {
            if (startType == CellType_O)
            {
                return Result_WinO;
            }
            else if (startType == CellType_X)
            {
                return Result_WinX;
            }
        }
    }

    if (isDraw)
    {
        return Result_Draw;
    }
    else
    {
        return Result_NotCompleted;
    }
}

int main(int argc, char** argv)
{
	if (argc != 2) {
		std::cerr << "invalid argument!" << std::endl;
	}
	
	char filePathBuf[255];
	
	sprintf(filePathBuf, "%s.in\0", argv[1]);	
	FILE* inputFile = fopen(filePathBuf, "r");
	if (inputFile == NULL) 
	{
		std::cerr << "input file open error!" << std::endl;
		exit(0);
	}
	
	sprintf(filePathBuf, "%s.out\0", argv[1]);
	FILE* outputFile = fopen(filePathBuf, "w");
	if (outputFile == NULL)
	{
		std::cerr << "output file open error!" << std::endl;
		exit(0);
	}
	
	int num = 0;
	fscanf(inputFile, "%d\n", &num);
    
    Board* board = new Board[num];
	for (int idx = 0; idx < num; ++idx)
	{
	    for (int y = 0; y < CELL_HEIGHT; ++y)
	    {
	        char temp[CELL_WIDTH];
	        fscanf(inputFile, "%c%c%c%c\n", &temp[0], &temp[1], &temp[2], &temp[3]);

	        for (int x = 0; x < CELL_WIDTH; ++x)
	        {
	            CellType tempCellType = CellType_S;
	            switch(temp[x])
	            {
	            case 'O':
	                tempCellType = CellType_O;
	                break;
	            case 'X':
	                tempCellType = CellType_X;
	                break;
	            case 'T':
	                tempCellType = CellType_T;
	                break;
	            case '.':
	                tempCellType = CellType_S;
	                break;
	            default:
	                break;
	            }
	            board[idx].a[y][x] = tempCellType;
	        }
	    }
	    
	    Result result = CheckBoard(board[idx]);
	    
	    const char* resultStr = null;

	    switch(result)
	    {
	    case Result_WinO:
	        resultStr = "O won";
	        break;
	    case Result_WinX:
	        resultStr = "X won";
	        break;
	    case Result_Draw:
	        resultStr = "Draw";
	        break;
	    case Result_NotCompleted:
	        resultStr = "Game has not completed";
	        break;
	    }

		fprintf(outputFile, "Case #%d: %s\n", idx + 1, resultStr);
	}
    delete[] board;
	
	fclose(outputFile);
	fclose(inputFile);
	
	return 0;
}
