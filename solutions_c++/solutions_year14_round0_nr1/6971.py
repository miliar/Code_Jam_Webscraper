#ifndef GOOGLE_JAM_IO_H
#define GOOGLE_JAM_IO_H

#include <Global.h>
#include <fstream>

namespace GOOGLE_JAM
{
    class Output
    {
    public:
        Output(const std::string &filename);

        void write(const std::string &data);

    private:
        uint32 m_uiRound;
        std::ofstream m_File;
    };

    class Input
    {
    public:
        Input();

        void open(const std::string &filename);

        //************************************
        // Description: Fill "result" with a number of strings. The number of strings is the first parsed line.
        //************************************
        StringVector nextDataset(uint32 elementCount = 0);
        //************************************
        // Description: Fill "result" with a number of uint32. The number of line is the first parsed line.
        //          The second line will be stored in "specificData".
        //************************************
        void nextDataset(UInt32Vector2D &result, UInt32Vector &specificData);
        void nextDataset(UInt32Vector &result);
        void nextDataset(UInt64Vector &result);

        inline bool isOk() const { return m_File.good(); }

        inline uint32 getDataSetCount() const { return m_uiDataSets; }

    protected:
        std::ifstream m_File;

    private:
        uint32 m_uiDataSets;
    };
}
#endif